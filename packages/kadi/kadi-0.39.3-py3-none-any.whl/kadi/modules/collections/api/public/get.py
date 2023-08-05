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
from io import BytesIO

from flask_login import current_user
from flask_login import login_required

import kadi.lib.constants as const
from kadi.ext.db import db
from kadi.lib.api.blueprint import bp
from kadi.lib.api.core import check_access_token_scopes
from kadi.lib.api.core import json_error_response
from kadi.lib.api.core import json_response
from kadi.lib.api.core import scopes_required
from kadi.lib.api.utils import create_pagination_data
from kadi.lib.api.utils import status
from kadi.lib.conversion import lower
from kadi.lib.conversion import normalize
from kadi.lib.conversion import parse_boolean_string
from kadi.lib.conversion import parse_json_object
from kadi.lib.conversion import strip
from kadi.lib.db import escape_like
from kadi.lib.permissions.core import has_permission
from kadi.lib.permissions.utils import permission_required
from kadi.lib.resources.api import get_resource_group_roles
from kadi.lib.resources.api import get_resource_user_roles
from kadi.lib.resources.utils import get_linked_resources
from kadi.lib.revisions.schemas import ObjectRevisionSchema
from kadi.lib.web import download_bytes
from kadi.lib.web import download_stream
from kadi.lib.web import paginated
from kadi.lib.web import qparam
from kadi.lib.web import url_for
from kadi.modules.collections.export import get_export_data
from kadi.modules.collections.models import Collection
from kadi.modules.collections.models import CollectionState
from kadi.modules.collections.schemas import CollectionRevisionSchema
from kadi.modules.collections.schemas import CollectionSchema
from kadi.modules.collections.utils import get_child_collection_records
from kadi.modules.collections.utils import search_collections
from kadi.modules.records.models import Record
from kadi.modules.records.schemas import RecordSchema


@bp.get("/collections")
@login_required
@scopes_required("collection.read")
@paginated(page_max=100)
@qparam("query", parse=strip, description="A query to search the collections with.")
@qparam(
    "sort",
    default="_score",
    description="The order of the search results. One of ``_score``, ``last_modified``,"
    " ``-last_modified``, ``created_at``, ``-created_at``, ``title``, ``-title``,"
    " ``identifier`` or ``-identifier``. Falls back to ``-last_modified`` if no search"
    " query is given.",
)
@qparam(
    "visibility",
    description="A visibility value to filter the collections with. One of ``private``"
    " or ``public``.",
)
@qparam(
    "user",
    multiple=True,
    parse=int,
    description="User IDs to filter the collections with in relation to their creator."
    " All given users are filtered using an *OR* operation.",
)
@qparam(
    "tag",
    multiple=True,
    parse=[lower, normalize],
    description="Tags to filter the collections with. All given tags are filtered using"
    " the operator specified via the **tag_operator**.",
)
@qparam(
    "tag_operator",
    default="or",
    parse=[lower, strip],
    description="The operator to filter the tags with. One of ``or`` or ``and``.",
)
@status(200, "Return a paginated list of collections.")
def get_collections(page, per_page, qparams):
    """Search and filter for collections."""
    collections, total_collections = search_collections(
        search_query=qparams["query"],
        page=page,
        per_page=per_page,
        sort=qparams["sort"],
        visibility=qparams["visibility"],
        user_ids=qparams["user"],
        tags=qparams["tag"],
        tag_operator=qparams["tag_operator"],
    )

    data = {
        "items": CollectionSchema(many=True).dump(collections),
        "_actions": {"new_collection": url_for("api.new_collection")},
        **create_pagination_data(total_collections, page, per_page, **qparams),
    }

    return json_response(200, data)


@bp.get("/collections/<int:id>")
@permission_required("read", "collection", "id")
@scopes_required("collection.read")
@status(200, "Return the collection.")
def get_collection(id):
    """Get the collection specified by the given *id*."""
    collection = Collection.query.get_active_or_404(id)
    return json_response(200, CollectionSchema().dump(collection))


@bp.get("/collections/identifier/<identifier:identifier>")
@login_required
@scopes_required("collection.read")
@status(200, "Return the collection.")
def get_collection_by_identifier(identifier):
    """Get the collection specified by the given *identifier*."""
    collection = Collection.query.filter_by(
        identifier=identifier, state=CollectionState.ACTIVE
    ).first_or_404()

    if not has_permission(current_user, "read", "collection", collection.id):
        return json_error_response(403)

    return json_response(200, CollectionSchema().dump(collection))


@bp.get("/collections/<int:id>/records")
@permission_required("read", "collection", "id")
@scopes_required("collection.read", "record.read")
@paginated
@qparam(
    "filter",
    parse=normalize,
    description="A query to filter the records by their title or identifier.",
)
@qparam(
    "action",
    multiple=True,
    description="Further actions the current user needs permission to perform in the"
    " linked records.",
)
@qparam(
    "children",
    default=False,
    parse=parse_boolean_string,
    description="Flag indicating whether records of child collections should be"
    " included in the results.",
)
@status(
    200,
    "Return a paginated list of records, sorted by last modification date in descending"
    " order.",
)
def get_collection_records(id, page, per_page, qparams):
    """Get the records the collection specified by the given *id* contains."""
    collection = Collection.query.get_active_or_404(id)

    if qparams["children"]:
        records_query = get_child_collection_records(
            collection, actions=qparams["action"]
        )
    else:
        records_query = get_linked_resources(
            Record, collection.records, actions=qparams["action"]
        )

    filter_term = escape_like(qparams["filter"])
    paginated_records = (
        records_query.filter(
            db.or_(
                Record.title.ilike(f"%{filter_term}%"),
                Record.identifier.ilike(f"%{filter_term}%"),
            ),
        )
        .order_by(Record.last_modified.desc())
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    data = {
        "items": RecordSchema(many=True, linked_collection=collection).dump(
            paginated_records
        ),
        **create_pagination_data(
            paginated_records.total, page, per_page, id=collection.id, **qparams
        ),
    }

    return json_response(200, data)


@bp.get("/collections/<int:id>/collections")
@permission_required("read", "collection", "id")
@scopes_required("collection.read")
@paginated
@qparam(
    "filter",
    parse=normalize,
    description="A query to filter the collections by their title or identifier.",
)
@qparam(
    "action",
    multiple=True,
    description="Further actions the current user needs permission to perform in the"
    " child collections.",
)
@status(
    200,
    "Return a paginated list of collections, sorted by last modification date in"
    " descending order.",
)
def get_child_collections(id, page, per_page, qparams):
    """Get the child collections of the collection specified by the given *id*."""
    collection = Collection.query.get_active_or_404(id)

    filter_term = escape_like(qparams["filter"])
    paginated_collections = (
        get_linked_resources(Collection, collection.children, actions=qparams["action"])
        .filter(
            db.or_(
                Collection.title.ilike(f"%{filter_term}%"),
                Collection.identifier.ilike(f"%{filter_term}%"),
            ),
        )
        .order_by(Collection.last_modified.desc())
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    data = {
        "items": CollectionSchema(many=True, parent_collection=collection).dump(
            paginated_collections
        ),
        **create_pagination_data(
            paginated_collections.total, page, per_page, id=collection.id, **qparams
        ),
    }

    return json_response(200, data)


@bp.get("/collections/<int:id>/roles/users")
@permission_required("read", "collection", "id")
@scopes_required("collection.read", "user.read")
@paginated
@qparam(
    "filter",
    parse=strip,
    description="A query to filter the users by their username or display name.",
)
@qparam("exclude", multiple=True, parse=int, description="User IDs to exclude.")
@status(
    200,
    "Return a paginated list of user roles, sorted by role name and then by user ID in"
    " ascending order. The creator will always be listed first.",
)
def get_collection_user_roles(id, page, per_page, qparams):
    """Get the user roles of the collection specified by the given *id*."""
    collection = Collection.query.get_active_or_404(id)

    items, total = get_resource_user_roles(
        collection,
        page=page,
        per_page=per_page,
        filter_term=qparams["filter"],
        exclude=qparams["exclude"],
    )
    data = {
        "items": items,
        **create_pagination_data(total, page, per_page, id=collection.id),
    }

    return json_response(200, data)


@bp.get("/collections/<int:id>/roles/groups")
@permission_required("read", "collection", "id")
@scopes_required("collection.read", "group.read")
@paginated
@qparam(
    "filter",
    parse=normalize,
    description="A query to filter the groups by their title or identifier.",
)
@status(
    200,
    "Return a paginated list of group roles, sorted by role name and then by group ID"
    " in ascending order.",
)
def get_collection_group_roles(id, page, per_page, qparams):
    """Get the group roles of the collection specified by the given *id*.

    If a user can manage permissions of this collection, all group roles are returned.
    However, groups that a user can normally not read include only a limited subset of
    attributes.
    """
    collection = Collection.query.get_active_or_404(id)

    items, total = get_resource_group_roles(
        collection, page=page, per_page=per_page, filter_term=qparams["filter"]
    )
    data = {
        "items": items,
        **create_pagination_data(total, page, per_page, id=collection.id),
    }

    return json_response(200, data)


@bp.get("/collections/<int:id>/revisions")
@permission_required("read", "collection", "id")
@scopes_required("collection.read")
@paginated
@status(
    200,
    "Return a paginated list of revisions, sorted by revision timestamp in descending"
    " order.",
)
def get_collection_revisions(id, page, per_page):
    """Get the revisions of the collection specified by the given *id*."""
    collection = Collection.query.get_active_or_404(id)
    paginated_revisions = collection.ordered_revisions.paginate(
        page=page, per_page=per_page, error_out=False
    )

    schema = ObjectRevisionSchema(
        CollectionRevisionSchema,
        many=True,
        api_endpoint="api.get_collection_revision",
        view_endpoint="collections.view_revision",
        endpoint_args={"collection_id": collection.id},
    )
    data = {
        "items": schema.dump(paginated_revisions),
        **create_pagination_data(
            paginated_revisions.total, page, per_page, id=collection.id
        ),
    }

    return json_response(200, data)


@bp.get("/collections/<int:collection_id>/revisions/<int:revision_id>")
@permission_required("read", "collection", "collection_id")
@scopes_required("collection.read")
@qparam(
    "revision",
    default=None,
    parse=int,
    description="The ID of a revision to compare with instead of the previous one.",
)
@status(200, "Return the revision.")
def get_collection_revision(collection_id, revision_id, qparams):
    """Get a collection revision.

    Will return the revision specified by the given *revision_id* of the collection
    specified by the given *collection_id*.
    """
    collection = Collection.query.get_active_or_404(collection_id)
    revision = collection.revisions.filter(
        Collection.revision_class.id == revision_id
    ).first_or_404()

    compared_revision = None

    if qparams["revision"]:
        compared_revision = collection.revisions.filter(
            Collection.revision_class.id == qparams["revision"]
        ).first()

    schema = ObjectRevisionSchema(
        CollectionRevisionSchema,
        compared_revision=compared_revision,
        api_endpoint="api.get_collection_revision",
        view_endpoint="collections.view_revision",
        endpoint_args={"collection_id": collection.id},
    )

    return json_response(200, schema.dump(revision))


@bp.get("/collections/<int:id>/export/<export_type>")
@permission_required("read", "collection", "id")
@scopes_required("collection.read")
@qparam(
    "filter",
    default=lambda: {},
    parse=parse_json_object,
    description="An URL-encoded JSON object to specify various filters to adjust"
    " the returned export data. See the ``export_filter`` parameter in"
    " :func:`kadi.modules.collections.export.get_export_data` for a more detailed"
    " description (in Python syntax).",
)
@status(200, "Return the exported collection data.")
def get_collection_export(id, export_type, qparams):
    """Export the collection specified by the given *id*.

    Currently, ``json``, ``rdf``, ``qr`` and ``ro-crate`` are supported as export types.
    """
    collection = Collection.query.get_active_or_404(id)
    export_types = const.EXPORT_TYPES["collection"]

    if export_type not in export_types:
        return json_error_response(404)

    export_filter = qparams["filter"]

    # Always exclude certain information if the access token scopes are insufficient.
    if not check_access_token_scopes("user.read"):
        export_filter["user"] = True
    if not check_access_token_scopes("record.read"):
        export_filter["records"] = True

    data = get_export_data(collection, export_type, export_filter=export_filter)

    file_ext = export_types[export_type]["ext"]
    download_name = f"{collection.identifier}.{file_ext}"

    if export_type == "ro-crate":
        if not isinstance(data, BytesIO):
            return download_stream(
                data,
                download_name,
                mimetype=const.MIMETYPE_ZIP,
                content_length=len(data),
            )

        download_name = f"{collection.identifier}.jsonld"

    return download_bytes(data, download_name)
