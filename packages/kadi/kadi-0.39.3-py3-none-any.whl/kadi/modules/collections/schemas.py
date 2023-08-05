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
from flask import has_request_context
from flask_login import current_user
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import post_load
from marshmallow import validates
from marshmallow.validate import Length
from marshmallow.validate import OneOf
from marshmallow.validate import ValidationError

from .models import Collection
from kadi.lib.api.core import check_access_token_scopes
from kadi.lib.conversion import lower
from kadi.lib.conversion import normalize
from kadi.lib.conversion import strip
from kadi.lib.permissions.core import has_permission
from kadi.lib.schemas import check_duplicate_identifier
from kadi.lib.schemas import FilteredString
from kadi.lib.schemas import KadiSchema
from kadi.lib.schemas import SortedPluck
from kadi.lib.schemas import validate_identifier
from kadi.lib.tags.schemas import TagSchema
from kadi.lib.web import url_for
from kadi.modules.accounts.schemas import UserSchema
from kadi.modules.records.schemas import RecordSchema


class CollectionSchema(KadiSchema):
    """Schema to represent collections.

    See :class:`.Collection`.

    :param previous_collection: (optional) A collection whose identifier should be
        excluded when checking for duplicates while deserializing.
    :param linked_record: (optional) A record that is linked to each collection that
        should be serialized. Will be used to build endpoints for corresponding
        actions.
    :param parent_collection: (optional) A collection that is the parent of each
        collection that should be serialized. Will be used to build endpoints for
        corresponding actions.
    """

    id = fields.Integer(required=True)

    identifier = FilteredString(
        required=True,
        filter=[lower, strip],
        validate=[
            Length(
                max=Collection.Meta.check_constraints["identifier"]["length"]["max"]
            ),
            validate_identifier,
        ],
    )

    title = FilteredString(
        required=True,
        filter=normalize,
        validate=Length(
            max=Collection.Meta.check_constraints["title"]["length"]["max"]
        ),
    )

    description = fields.String(
        validate=Length(
            max=Collection.Meta.check_constraints["description"]["length"]["max"]
        )
    )

    visibility = fields.String(
        validate=OneOf(Collection.Meta.check_constraints["visibility"]["values"])
    )

    tags = SortedPluck(TagSchema, "name", many=True)

    plain_description = fields.String(dump_only=True)

    state = fields.String(dump_only=True)

    created_at = fields.DateTime(dump_only=True)

    last_modified = fields.DateTime(dump_only=True)

    creator = fields.Nested(UserSchema, dump_only=True)

    _links = fields.Method("_generate_links")

    _actions = fields.Method("_generate_actions")

    def __init__(
        self,
        previous_collection=None,
        linked_record=None,
        parent_collection=None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.previous_collection = previous_collection
        self.linked_record = linked_record
        self.parent_collection = parent_collection

    @validates("id")
    def _validate_id(self, value):
        if Collection.query.get_active(value) is None:
            raise ValidationError("No collection with this ID exists.")

    @validates("identifier")
    def _validate_identifier(self, value):
        check_duplicate_identifier(Collection, value, exclude=self.previous_collection)

    @post_load
    def _post_load(self, data, **kwargs):
        if "tags" in data:
            data["tags"] = sorted(list({tag["name"] for tag in data["tags"]}))

        return data

    @post_dump
    def _post_dump(self, data, **kwargs):
        if "creator" in data and not check_access_token_scopes("user.read"):
            del data["creator"]

        return data

    def _generate_links(self, obj):
        links = {
            "self": url_for("api.get_collection", id=obj.id),
            "records": url_for("api.get_collection_records", id=obj.id),
            "children": url_for("api.get_child_collections", id=obj.id),
            "user_roles": url_for("api.get_collection_user_roles", id=obj.id),
            "group_roles": url_for("api.get_collection_group_roles", id=obj.id),
            "revisions": url_for("api.get_collection_revisions", id=obj.id),
        }

        # Only include the parent link if the parent is readable by the current user.
        if obj.parent_id and (
            not has_request_context()
            or (
                current_user.is_authenticated
                and has_permission(current_user, "read", "collection", obj.parent_id)
            )
        ):
            links["parent"] = url_for("api.get_collection", id=obj.parent_id)

        if self._internal:
            links["view"] = url_for("collections.view_collection", id=obj.id)

        return links

    def _generate_actions(self, obj):
        actions = {
            "edit": url_for("api.edit_collection", id=obj.id),
            "delete": url_for("api.delete_collection", id=obj.id),
            "link_record": url_for("api.add_collection_record", id=obj.id),
            "link_collection": url_for("api.add_child_collection", id=obj.id),
            "add_user_role": url_for("api.add_collection_user_role", id=obj.id),
            "add_group_role": url_for("api.add_collection_group_role", id=obj.id),
        }

        if self.linked_record:
            actions["remove_link"] = url_for(
                "api.remove_record_collection",
                record_id=self.linked_record.id,
                collection_id=obj.id,
            )

        if self.parent_collection:
            actions["remove_link"] = url_for(
                "api.remove_child_collection",
                collection_id=self.parent_collection.id,
                child_id=obj.id,
            )

        return actions


class CollectionRevisionSchema(CollectionSchema):
    """Schema to represent collection revisions.

    Additionally includes the serialization of the default record template with a
    limited subset of attributes.
    """

    record_template = fields.Nested(RecordSchema, only=["id"], dump_only=True)
