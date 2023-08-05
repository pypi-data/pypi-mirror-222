# Copyright 2021 Karlsruhe Institute of Technology
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

import qrcode
from flask_login import current_user
from rdflib import Literal
from rdflib import RDF
from rdflib import SDO
from rdflib import URIRef

from .schemas import CollectionSchema
from kadi.lib.export import RDFGraph
from kadi.lib.resources.utils import get_linked_resources
from kadi.lib.utils import formatted_json
from kadi.lib.web import url_for
from kadi.modules.records.export import get_record_dict_data
from kadi.modules.records.export import RecordRDFGraph
from kadi.modules.records.export import RecordROCrate
from kadi.modules.records.models import Record


def get_dict_data(collection, export_filter, user):
    """Export a collection as a dictionary.

    See :func:`get_export_data` for an explanation of the parameters.

    :return: The exported collection as a dictionary.
    """
    exclude_attrs = ["_actions", "_links"]

    # Unnecessary attributes to exclude in all resources, also depending on whether user
    # information should be excluded.
    if export_filter.get("user", False):
        exclude_attrs.append("creator")
    else:
        exclude_attrs += [
            "creator.is_sysadmin",
            "creator.system_role",
            "creator._links",
            "creator._actions",
            "creator.identity.email",
            "creator.identity.email_confirmed",
        ]

    # Collect the basic metadata of the collection.
    schema = CollectionSchema(exclude=exclude_attrs)
    collection_data = schema.dump(collection)

    # If not excluded, include all records the collection contains as "records" by
    # reusing the record export functionality.
    if not export_filter.get("records", False):
        collection_data["records"] = []

        records = get_linked_resources(Record, collection.records, user=user).order_by(
            Record.last_modified.desc()
        )
        for record in records:
            record_data = get_record_dict_data(record, export_filter, user)
            collection_data["records"].append(record_data)

    return collection_data


def get_json_data(collection, export_filter, user):
    """Export a collection as a JSON file.

    See :func:`get_export_data` for an explanation of the parameters and return value.
    """
    collection_data = get_dict_data(collection, export_filter, user)
    json_data = formatted_json(collection_data)

    return BytesIO(json_data.encode())


def get_qr_data(collection):
    """Export a collection as a QR code in PNG format.

    See :func:`get_export_data` for an explanation of the parameters and return value.
    """
    image = qrcode.make(url_for("collections.view_collection", id=collection.id))

    image_data = BytesIO()
    image.save(image_data, format="PNG")
    image_data.seek(0)

    return image_data


def get_ro_crate_data(collection, export_filter, user):
    """Export a collection as an RO-Crate.

    See :func:`get_export_data` for an explanation of the parameters and return value.
    """

    # Check if records should be excluded, which only leaves us with the basic metadata
    # in the RO-Crate.
    if export_filter.get("records", False):
        records = []
    else:
        records = get_linked_resources(Record, collection.records, user=user).order_by(
            Record.last_modified.desc()
        )

    ro_crate = RecordROCrate(
        records, collection.identifier, export_filter=export_filter, user=user
    )

    if export_filter.get("metadata_only", False):
        return BytesIO(ro_crate.dump_metadata().encode())

    return ro_crate


def get_rdf_data(collection, export_filter, user):
    """Export a collection as an RDF graph in Turtle format.

    See :func:`get_export_data` for an explanation of the parameters and return value.
    """
    collection_data = get_dict_data(collection, export_filter=export_filter, user=user)

    c_graph = RDFGraph()
    c_ref = URIRef(url_for("collections.view_collection", id=collection.id))

    c_graph.add((c_ref, RDF.type, SDO.Collection))
    c_graph.add((c_ref, SDO.identifier, Literal(collection_data["identifier"])))
    c_graph.add((c_ref, SDO.name, Literal(collection_data["title"])))
    c_graph.add((c_ref, SDO.text, Literal(collection_data["description"])))
    c_graph.add((c_ref, SDO.dateCreated, Literal(collection_data["created_at"])))
    c_graph.add((c_ref, SDO.dateModified, Literal(collection_data["last_modified"])))

    for tag in collection_data["tags"]:
        c_graph.add((c_ref, SDO.keywords, Literal(tag)))

    if "creator" in collection_data:
        author_ref = c_graph.author_ref(collection_data["creator"])
        c_graph.add((c_ref, SDO.author, author_ref))

    if export_filter.get("records", False):
        records = []
    else:
        records = get_linked_resources(Record, collection.records, user=user)

    for record in records:
        c_graph.add(
            (c_ref, SDO.hasPart, URIRef(url_for("records.view_record", id=record.id)))
        )

    r_graph = RecordRDFGraph(records, export_filter=export_filter, user=user)

    try:
        rdf_data = (c_graph + r_graph).serialize(format="turtle")
    except:
        # Just in case, even if all IRIs should be valid.
        rdf_data = ""

    return BytesIO(rdf_data.encode())


def get_export_data(collection, export_type, export_filter=None, user=None):
    """Export a collection in a given format.

    :param collection: The collection to export.
    :param export_type: The export type, one of ``"json"``, ``"rdf"``, ``"qr"`` or
        ``"ro-crate"``.
    :param export_filter: (optional) A dictionary specifying various filters to adjust
        the returned export data, depending on the export type. Only usable in
        combination with the ``"json"``, ``"rdf"`` and ``"ro-crate"`` export types. Note
        that the values in the example below represent the respective default values.

        **Example:**

        .. code-block:: python3

            {
                # Whether user information about the creator of the collection or any
                # linked resource should be excluded.
                "user": False,
                # Whether to exclude information about records that are part of the
                # collection.
                "records": False,
                # Whether to exclude all (True), outgoing ("out") or incoming ("in")
                # links of records with other records when record information is not
                # excluded.
                "links": False,
                # To specify which kind of export data of records should be included in
                # an exported RO-Crate when using the "ro-crate" export type and record
                # information is not excluded. All other filters also apply to this
                # export data, as far as applicable.
                "export_data": ["json", "rdf"],
                # Whether to return only the metadata file of an exported RO-Crate when
                # using the "ro-crate" export type.
                "metadata_only": False,
            }

    :param user: (optional) The user to check for various access permissions when
        generating the export data. Defaults to the current user.
    :return: The exported collection data as an in-memory byte stream or ``None`` if an
        unknown export type was given. Note that for the ``ro-crate`` export type, the
        returned data is an iterable producing the actual data on the fly instead,
        unless only the metadata file is exported by specifying the corresponding export
        filter.
    """
    export_filter = export_filter if export_filter is not None else {}
    user = user if user is not None else current_user

    if export_type == "json":
        return get_json_data(collection, export_filter, user)

    if export_type == "qr":
        return get_qr_data(collection)

    if export_type == "rdf":
        return get_rdf_data(collection, export_filter, user)

    if export_type == "ro-crate":
        return get_ro_crate_data(collection, export_filter, user)

    return None
