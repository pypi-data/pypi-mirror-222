# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from contextlib import contextmanager

from flask import current_app
from flask import send_file
from flask_login import current_user
from sqlalchemy.exc import IntegrityError
from zipstream import ZipStream

import kadi.lib.constants as const
from .models import File
from .models import FileState
from .models import Record
from .models import RecordState
from .models import TemporaryFileState
from kadi.ext.db import db
from kadi.lib.db import acquire_lock
from kadi.lib.db import escape_like
from kadi.lib.db import update_object
from kadi.lib.permissions.core import get_permitted_objects
from kadi.lib.permissions.core import has_permission
from kadi.lib.revisions.core import create_revision as _create_revision
from kadi.lib.revisions.core import delete_revisions
from kadi.lib.storage.local import create_default_local_storage
from kadi.lib.validation import validate_mimetype
from kadi.lib.web import download_stream
from kadi.plugins.core import run_hook
from kadi.plugins.utils import signal_resource_change


def update_file(file, user=None, **kwargs):
    r"""Update an existing file.

    Note that this function issues a database commit or rollback.

    :param file: The file to update.
    :param user: (optional) The user who triggered the update. Defaults to the current
        user.
    :param \**kwargs: Keyword arguments that will be passed to
        :func:`kadi.lib.db.update_object`.
    :return: ``True`` if the file was updated successfully, ``False`` otherwise.
    """
    user = user if user is not None else current_user

    file = acquire_lock(file)

    if file.state != FileState.ACTIVE or file.record.state != RecordState.ACTIVE:
        # Release the file lock.
        db.session.commit()
        return False

    update_object(file, **kwargs)

    if db.session.is_modified(file):
        file.record.update_timestamp()

    try:
        db.session.flush()
    except IntegrityError:
        db.session.rollback()
        return False

    revision_created = _create_revision(file, user=user)

    # Releases the file lock as well.
    db.session.commit()

    if revision_created:
        signal_resource_change(file, user=user)

    return True


def delete_file(file, create_revision=True, user=None):
    """Delete an existing file.

    This will mark the file for deletion, i.e. only the file's state will be changed.
    Note that this function issues one or more database commits.

    :param file: The file to delete.
    :param create_revision: (optional) Flag indicating whether a revision should be
        created for the deletion.
    :param user: (optional) The user who triggered the deletion. Defaults to the current
        user.
    """
    from .uploads import delete_upload

    user = user if user is not None else current_user

    file = acquire_lock(file)
    file.state = FileState.INACTIVE

    if db.session.is_modified(file):
        file.record.update_timestamp()

    revision_created = False
    if create_revision:
        revision_created = _create_revision(file, user=user)

    # Mark any uploads related to the file for deletion as well.
    for upload in file.uploads:
        delete_upload(upload)

    # Releases the file lock as well.
    db.session.commit()

    if revision_created:
        signal_resource_change(file, user=user)


def remove_file(file, delete_from_db=True):
    """Remove a file from storage and optionally from the database.

    Note that this function issues one or more database commits.

    :param file: The file to remove.
    :param delete_from_db: (optional) A flag indicating whether the file should be
        deleted from the database as well, instead of just doing a soft deletion.
    """
    from .uploads import remove_upload

    delete_file(file, create_revision=False)

    # Remove any uploads related to the file as well.
    for upload in file.uploads:
        remove_upload(upload)

    storage = file.storage
    filepath = storage.create_filepath(str(file.id))

    storage.delete(filepath)

    if delete_from_db:
        delete_revisions(file)
        db.session.delete(file)
    else:
        file.state = FileState.DELETED

    db.session.commit()


@contextmanager
def open_file(file, mode="rb", encoding=None):
    """Context manager that yields an open file.

    **Example:**

    .. code-block:: python3

        with open_file(file) as file_object:
            pass

    :param file: The file to open.
    :param mode: (optional) The mode to open the file with.
    :param encoding: (optional) The encoding of the file if opening it in text mode.
    """
    storage = file.storage
    filepath = storage.create_filepath(str(file.id))

    f = storage.open(filepath, mode=mode, encoding=encoding)

    try:
        yield f
    finally:
        storage.close(f)


def download_file(file):
    """Send a file to a client for downloading.

    :param file: The file to download.
    :return: The response object.
    """
    storage = file.storage
    filepath = storage.create_filepath(str(file.id))

    # Passing a file path instead of an already opened file is required to use
    # "X-Sendfile", which will probably require special handling for different storages
    # in the future. Furthermore, the "conditional" flag seems to be only necessary when
    # using the development server to support range responses, otherwise the web server
    # handles that via "X-Sendfile".
    return send_file(
        filepath,
        mimetype=file.mimetype,
        download_name=file.name,
        as_attachment=True,
        etag=False,
        conditional=current_app.environment == const.ENV_DEVELOPMENT,
    )


def stream_files(record):
    """Stream all files of a record to a client as ZIP archive for downloading.

    :param record: The record the files belong to.
    :return: The response object.
    """
    zip_stream = ZipStream(sized=True)

    for file in record.active_files:
        filepath = file.storage.create_filepath(str(file.id))
        filename = file.name.replace("/", "_")

        zip_stream.add_path(filepath, arcname=filename)

    return download_stream(
        zip_stream, f"{record.identifier}.zip", content_length=len(zip_stream)
    )


def get_custom_mimetype(file, base_mimetype=None):
    """Get a custom MIME type of a file based on its content.

    Uses the :func:`kadi.plugins.spec.kadi_get_custom_mimetype` plugin hook for custom
    MIME types based on the file's content.

    :param file: The file to get the MIME type of.
    :param base_mimetype: (optional) The base MIME type of the file on which to base the
        custom MIME type.
    :return: The custom MIME type or ``None`` if no valid custom MIME type was found.
    """
    if base_mimetype is None:
        storage = file.storage

        filepath = storage.create_filepath(str(file.id))
        base_mimetype = storage.get_mimetype(filepath)

    try:
        custom_mimetype = run_hook(
            "kadi_get_custom_mimetype", file=file, base_mimetype=base_mimetype
        )
        if custom_mimetype is None:
            return None

        validate_mimetype(custom_mimetype)

    except Exception as e:
        current_app.logger.exception(e)
        return None

    return custom_mimetype


def get_direct_upload_type(file):
    """Get the direct upload type of a file.

    This type can be used to determine whether a file can be directly edited via a
    corresponding editor in the frontend. Such files must have a certain format and must
    not exceed a size of 10 MB.

    :param file: The file to get the direct upload type of.
    :return: The direct upload type or ``None`` if no suitable type can be determined.
    """
    if file.size <= 10 * const.ONE_MB:
        if file.magic_mimetype in const.IMAGE_MIMETYPES:
            return "drawing"

        if file.magic_mimetype.startswith("text/") or file.magic_mimetype in [
            const.MIMETYPE_JSON,
            const.MIMETYPE_XML,
            const.MIMETYPE_TOOL,
        ]:
            try:
                # As only UTF-8 encoded files are supported for direct editing, try to
                # read a decent amount of data using this encoding first.
                with open_file(file, mode="r", encoding="utf-8") as f:
                    f.read(const.ONE_MB)
                    return "text"
            except:
                pass

        elif file.magic_mimetype == const.MIMETYPE_FLOW:
            return "workflow"

    return None


def get_permitted_files(filter_term="", record_id=None, user=None):
    """Convenience function to get all active record files that a user can access.

    In this context having access to a file means having read permission for the record
    the file belongs to.

    :param filter_term: (optional) A (case insensitive) term to filter the files by
        their name or record identifier.
    :param record_id: (optional) A record ID by which to filter the files.
    :param user: (optional) The user to check for access permissions. Defaults to the
        current user.
    :return: The permitted file objects as query.
    """
    user = user if user is not None else current_user

    filter_term = escape_like(filter_term)
    record_ids_filter = []

    if record_id is not None:
        record = Record.query.get_active(record_id)

        if record is not None and has_permission(user, "read", "record", record.id):
            record_ids_filter = [record.id]
    else:
        record_ids_filter = (
            get_permitted_objects(user, "read", "record")
            .filter(Record.state == RecordState.ACTIVE)
            .with_entities(Record.id)
        )

    files_query = File.query.join(Record).filter(
        File.state == FileState.ACTIVE,
        Record.id.in_(record_ids_filter),
        db.or_(
            File.name.ilike(f"%{filter_term}%"),
            Record.identifier.ilike(f"%{filter_term}%"),
        ),
    )

    return files_query


def download_temporary_file(temporary_file):
    """Send a temporary file to a client as attachment for download.

    :param temporary_file: The :class:`.TemporaryFile` to download.
    :return: The response object.
    """
    storage = create_default_local_storage()
    filepath = storage.create_filepath(str(temporary_file.id))

    return send_file(
        filepath,
        mimetype=temporary_file.mimetype,
        download_name=temporary_file.name,
        as_attachment=True,
        etag=False,
    )


def remove_temporary_file(temporary_file):
    """Remove a temporary file from storage and from the database.

    Note that this function may issue one or more database commits.

    :param temporary_file: The :class:`.TemporaryFile` to remove.
    """
    temporary_file.state = TemporaryFileState.INACTIVE
    db.session.commit()

    storage = create_default_local_storage()
    filepath = storage.create_filepath(str(temporary_file.id))

    storage.delete(filepath)

    db.session.delete(temporary_file)
    db.session.commit()
