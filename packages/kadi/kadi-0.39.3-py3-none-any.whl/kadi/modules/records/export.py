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
import mimetypes
import os
from copy import deepcopy
from io import BytesIO
from urllib.parse import quote

import qrcode
from flask import json
from flask_babel import gettext as _
from flask_login import current_user
from rdflib import BNode
from rdflib import Literal
from rdflib import Namespace
from rdflib import RDF
from rdflib import RDFS
from rdflib import SDO
from rdflib import URIRef
from rdflib import XSD
from rdflib.collection import Collection as RDFCollection

import kadi.lib.constants as const
from .extras import is_nested_type
from .links import get_permitted_record_links
from .models import File
from .models import RecordLink
from .schemas import FileSchema
from .schemas import RecordLinkSchema
from .schemas import RecordSchema
from kadi.lib.conversion import parse_datetime_string
from kadi.lib.export import PDF
from kadi.lib.export import RDFGraph
from kadi.lib.export import ROCrate
from kadi.lib.format import filesize
from kadi.lib.format import pretty_type_name
from kadi.lib.utils import formatted_json
from kadi.lib.utils import is_iterable
from kadi.lib.utils import utcnow
from kadi.lib.web import url_for


class RecordPDF(PDF):
    """Record PDF export class.

    :param record: The record to generate the PDF from.
    :param export_filter: (optional) See :func:`get_record_export_data`.
    :param user: (optional) The user to check for various access permissions when
        generating the PDF. Defaults to the current user.
    """

    def __init__(self, record, export_filter=None, user=None):
        super().__init__(title=record.title)

        self.record = record
        self.export_filter = export_filter if export_filter is not None else {}
        self.user = user if user is not None else current_user

        self.print_overview()
        self.ln(h=15)
        self.print_extras()
        self.ln(h=15)
        self.print_files()

        if self.export_filter.get("links", False) is not True:
            self.ln(h=15)
            self.print_record_links()

    def _print_heading(self, txt):
        # Basic heuristic to try avoiding widowed headings.
        if self.will_page_break(self.font_size + 10):
            self.add_page()

        self.start_section(txt)
        self.set_font(size=10, style="B")
        self.write(txt=txt)
        self.ln(h=self.font_size + 1)
        self.set_draw_color(r=150, g=150, b=150)
        self.line(self.l_margin, self.y, self.w - self.r_margin, self.y)
        self.set_draw_color(r=0, g=0, b=0)

    def _print_placeholder(self, txt):
        self.set_font(size=10, style="I")
        self.set_text_color(r=150, g=150, b=150)
        self.write(txt=txt)
        self.set_text_color(r=0, g=0, b=0)
        self.ln()

    def print_overview(self):
        """Print the record overview, i.e. the basic metadata of the record."""
        self.start_section(_("Overview"))

        # Top right header content.
        image_size = 20
        view_record_url = url_for("records.view_record", id=self.record.id)
        image = qrcode.make(view_record_url)
        cursor_x = self.x
        cursor_y = self.y
        start_x = self.w - self.r_margin - image_size

        self.image(
            image.get_image(),
            x=start_x,
            y=cursor_y,
            w=image_size,
            h=image_size,
            link=view_record_url,
        )
        self.rect(start_x, cursor_y, image_size, image_size)
        self.set_xy(start_x, cursor_y + image_size + 2)
        self.set_font(size=8)
        self.set_text_color(r=150, g=150, b=150)
        self.cell(w=image_size, txt=f"ID: {self.record.id}", align="C")
        self.set_text_color(r=0, g=0, b=0)
        self.set_xy(cursor_x, cursor_y)

        # Top left header content.
        cell_width = self.epw * 0.85

        self.set_font(size=13, style="B")
        self.multi_cell(cell_width, txt=self.record.title, align="L")
        self.ln(h=2)

        self.set_font(size=10)
        self.multi_cell(cell_width, txt=f"@{self.record.identifier}", align="L")
        self.ln(h=5)

        if self.record.type:
            self.set_font(style="B")
            self.multi_cell(
                cell_width, txt="{}: {}".format(_("Type"), self.record.type), align="L"
            )
            self.ln(h=15)
        else:
            self.ln(h=10)

        # Description.
        if self.record.description:
            self.set_font(family="DejaVuSansMono")
            self.write(txt=self.record.description)
            self.set_font(family="DejaVuSans")
        else:
            self._print_placeholder(_("No description."))

        self.ln(h=self.font_size + 15)

        # Creator.
        if not self.export_filter.get("user", False):
            self.set_font(size=10)
            self.write(txt="{} ".format(_("Created by")))
            self.set_font(style="B")
            self.write(
                txt=self.record.creator.identity.displayname,
                link=url_for("accounts.view_user", id=self.record.creator.id),
            )
            self.ln(h=self.font_size + 3)

        # Creation date.
        self.set_font()
        self.write(
            txt="{} {}".format(
                _("Created at"), self.format_date(self.record.created_at)
            )
        )
        self.ln(h=self.font_size)

        # License and tags.
        if self.record.license or self.record.tags.count() > 0:
            self.ln(h=5)
            self.set_draw_color(r=150, g=150, b=150)
            self.line(self.l_margin, self.y, self.w - self.r_margin, self.y)
            self.set_draw_color(r=0, g=0, b=0)
            self.ln(h=5)

            if self.record.license:
                self.set_font(style="B")
                self.write(txt="{}: ".format(_("License")))
                self.set_font()
                self.write(txt=self.record.license.title, link=self.record.license.url)
                self.ln()

            if self.record.tags.count() > 0:
                if self.record.license:
                    self.ln(h=3)

                self.set_font(style="B")
                self.write(txt="{}: ".format(_("Tags")))
                self.set_font()
                self.write(
                    txt="; ".join(tag.name for tag in self.record.tags.order_by("name"))
                )
                self.ln()

    def print_extras(self):
        """Print the extra metadata of the record."""
        self._print_heading(_("Extra metadata"))
        self.ln(h=5)

        extras = self.record.extras
        excluded_extras = self.export_filter.get("extras")

        if excluded_extras:
            extras = filter_extras(extras, excluded_extras)

        if extras:
            self.set_font(size=9)
            self.set_draw_color(r=200, g=200, b=200)
            self._print_extras(extras)
            self.set_draw_color(r=0, g=0, b=0)
        else:
            self._print_placeholder(txt=_("No extra metadata."))

    def _print_extras(self, extras, depth=0):
        for index, extra in enumerate(extras):
            self._print_extra(index, extra, depth)

            if is_nested_type(extra["type"]):
                self._print_extras(extra["value"], depth=depth + 1)

        if depth == 0:
            self.line(self.l_margin, self.y, self.w - self.r_margin, self.y)

    def _set_nested_color(self, depth):
        if depth % 2 == 1:
            self.set_fill_color(r=240, g=240, b=240)
        else:
            self.set_fill_color(r=255, g=255, b=255)

    def _print_extra(self, index, extra, depth):
        nested_margin = 5
        column_width = (self.epw - nested_margin * depth) / 10

        # Calculate the maximum height the cells require.
        key_width = column_width * 8
        value_width = 0
        unit_width = 0
        type_width = column_width * 2

        key_txt = extra.get("key", f"({index + 1})")
        value_txt = ""
        unit_txt = ""
        type_txt = pretty_type_name(extra["type"]).capitalize()

        if not is_nested_type(extra["type"]):
            key_width = column_width * 4

            if extra.get("unit"):
                value_width = column_width * 3
                unit_width = column_width
                unit_txt = extra["unit"]
            else:
                value_width = column_width * 4

            value_txt = json.dumps(extra["value"])

            if extra["value"] is not None:
                if extra["type"] == "str":
                    value_txt = extra["value"]
                elif extra["type"] == "date":
                    date_time = parse_datetime_string(extra["value"])
                    value_txt = self.format_date(date_time, include_micro=True)

        max_height = self.calculate_max_height(
            [
                (key_width, key_txt, "B" if is_nested_type(extra["type"]) else ""),
                (value_width, value_txt, ""),
                (unit_width, unit_txt, ""),
                (type_width, type_txt, ""),
            ]
        )
        cell_height = max_height + 2
        page_break = False

        if self.will_page_break(cell_height):
            self.line(self.l_margin, self.y, self.w - self.r_margin, self.y)
            self.add_page()
            page_break = True

        cursor_y = self.y

        # Print the "boxes" of the nested parent metadata entry, which automatically
        # gives us the correct left margin.
        for i in range(0, depth):
            self._set_nested_color(i)
            self.cell(w=nested_margin, h=cell_height, border="L", fill=True)

        self._set_nested_color(depth)

        if is_nested_type(extra["type"]):
            self.set_font(style="B")
            key_border = "LT"
        else:
            key_border = "LTB"

        cursor_x = self.x
        self.cell(w=key_width, h=cell_height, border=key_border, fill=True)
        self.set_xy(cursor_x, cursor_y + 1)
        self.multi_cell(key_width, txt=key_txt, align="L")
        self.set_xy(self.x, cursor_y)
        self.set_font()

        if not is_nested_type(extra["type"]):
            if extra["value"] is None:
                self.set_font(style="I")

            cursor_x = self.x
            self.cell(w=value_width, h=cell_height, border="TB", fill=True)
            self.set_xy(cursor_x, cursor_y + 1)
            self.multi_cell(value_width, txt=value_txt, align="L")
            self.set_xy(self.x, cursor_y)
            self.set_font()

            if extra.get("unit"):
                cursor_x = self.x
                self.cell(w=unit_width, h=cell_height, border="TB", fill=True)
                self.set_xy(cursor_x, cursor_y + 1)
                self.set_text_color(r=150, g=150, b=150)
                self.multi_cell(unit_width, txt=unit_txt, align="R")
                self.set_xy(self.x, cursor_y)

        if is_nested_type(extra["type"]):
            type_border = "RT"
        else:
            type_border = "RTB"

        cursor_x = self.x
        self.cell(w=type_width, h=cell_height, border=type_border, fill=True)
        self.set_xy(cursor_x, cursor_y + 1)
        self.set_text_color(r=150, g=150, b=150)
        self.multi_cell(type_width, txt=type_txt, align="R")
        self.set_text_color(r=0, g=0, b=0)
        self.set_y(cursor_y)
        self.ln(h=cell_height)

        # Draw this line at the end so it is completely on top of the cells.
        if page_break:
            self.line(self.l_margin, cursor_y, self.w - self.r_margin, cursor_y)

    def print_files(self):
        """Print the files of the record."""
        self._print_heading(_("Files"))

        if self.record.active_files.count() > 0:
            self.set_font()

            for file in self.record.active_files.order_by(File.last_modified.desc()):
                self.ln(h=5)

                # Calculate the maximum height the cells require.
                name_width = self.epw * 0.85
                size_width = self.epw * 0.15

                name_txt = file.name
                size_txt = filesize(file.size)

                max_height = self.calculate_max_height(
                    [(name_width, name_txt, ""), (size_width, size_txt, "")]
                )

                if self.will_page_break(max_height):
                    self.add_page()

                cursor_y = self.y

                self.multi_cell(
                    name_width,
                    txt=name_txt,
                    link=url_for(
                        "records.view_file", record_id=self.record.id, file_id=file.id
                    ),
                    align="L",
                    new_y="TOP",
                )
                self.set_text_color(r=150, g=150, b=150)
                self.multi_cell(size_width, txt=size_txt, align="R")
                self.set_text_color(r=0, g=0, b=0)
                self.set_y(cursor_y)
                self.ln(h=max_height)
        else:
            self.ln(h=5)
            self._print_placeholder(txt=_("No files."))

    def print_record_links(self):
        """Print the links of the record with other records."""
        self._print_heading(_("Record links"))

        direction = None
        excluded_links = self.export_filter.get("links", False)

        if excluded_links == "in":
            direction = "out"
        elif excluded_links == "out":
            direction = "in"

        record_links = get_permitted_record_links(
            self.record, direction=direction, user=self.user
        ).order_by(RecordLink.created_at.desc())

        if record_links.count() > 0:
            for record_link in record_links:
                self.set_font()
                self.ln(h=5)

                # Calculate the maximum height the cells require.
                record_width = self.epw * 0.35
                link_width = self.epw * 0.3

                record_from_txt = f"@{record_link.record_from.identifier}"
                record_link_txt = record_link.name
                record_to_txt = f"@{record_link.record_to.identifier}"

                max_height = self.calculate_max_height(
                    [
                        (record_width, record_from_txt, ""),
                        (link_width, record_link_txt, ""),
                        (record_width, record_to_txt, ""),
                    ]
                )

                if self.will_page_break(max_height):
                    self.add_page()

                cursor_y = self.y

                if record_link.record_from == self.record:
                    self.set_font(style="I")

                self.multi_cell(
                    record_width,
                    txt=f"@{record_link.record_from.identifier}",
                    link=url_for("records.view_record", id=record_link.record_from.id),
                    align="L",
                    new_y="TOP",
                )
                self.set_font()
                self.set_text_color(r=150, g=150, b=150)
                # Just take the outgoing record as a base for the link overview URL.
                self.multi_cell(
                    link_width,
                    txt=record_link.name,
                    link=url_for(
                        "records.view_record_link",
                        record_id=record_link.record_from_id,
                        link_id=record_link.id,
                    ),
                    align="C",
                    new_y="TOP",
                )
                self.set_text_color(r=0, g=0, b=0)

                if record_link.record_to == self.record:
                    self.set_font(style="I")

                self.multi_cell(
                    record_width,
                    txt=f"@{record_link.record_to.identifier}",
                    link=url_for("records.view_record", id=record_link.record_to.id),
                    align="R",
                )
                self.set_y(cursor_y)
                self.ln(h=max_height)
        else:
            self.ln(h=5)
            self._print_placeholder(txt=_("No record links."))


class RecordRDFGraph(RDFGraph):
    """Record RDF graph export class."""

    def __init__(self, record_or_records, export_filter=None, user=None):
        super().__init__()

        self.export_filter = export_filter if export_filter is not None else {}
        self.user = user if user is not None else current_user

        if not is_iterable(record_or_records):
            record_or_records = [record_or_records]

        for record in record_or_records:
            self.add_record_metadata(record)

    def _extras_node(self, extras, record_ns, nested_type=None):
        extras_node = BNode()

        # This collection is only defined and used when we are within a (nested) list.
        list_collection = None

        if nested_type == "list":
            list_collection = RDFCollection(self, extras_node)

        for index, extra in enumerate(extras):
            extra_ref = None
            list_value_node = None

            if list_collection is None:
                extra_key = quote(extra.get("key", str(index)), safe="")
                extra_ref = record_ns[extra_key]

                if "term" in extra:
                    extra_ref = URIRef(extra["term"])
            else:
                # In order to include the potential terms of list values, we use a blank
                # node with rdf:predicate and rdf:object for term and value (depending
                # on the type), respectively.
                list_value_node = BNode()

                if "term" in extra:
                    self.add((list_value_node, RDF.predicate, URIRef(extra["term"])))

                list_collection.append(list_value_node)

            if is_nested_type(extra["type"]):
                nested_node = self._extras_node(
                    extra["value"], record_ns, nested_type=extra["type"]
                )

                if list_collection is None:
                    self.add((extras_node, extra_ref, nested_node))
                else:
                    self.add((list_value_node, RDF.object, nested_node))

            # None values are currently ignored.
            elif extra["value"] is not None:
                # By default, we use the type mapping of RDFLib.
                datatype = None

                if extra["type"] == "date":
                    datatype = XSD.dateTime

                # Numeric values use a blank node to also include their unit, if
                # applicable.
                if extra["type"] in {"int", "float"}:
                    extra_value = BNode()

                    self.add((extra_value, RDF.type, SDO.QuantitativeValue))
                    self.add(
                        (
                            extra_value,
                            SDO.value,
                            Literal(extra["value"], datatype=datatype),
                        )
                    )

                    if extra["unit"] is not None:
                        self.add((extra_value, SDO.unitText, Literal(extra["unit"])))
                else:
                    extra_value = Literal(extra["value"], datatype=datatype)

                if list_collection is None:
                    self.add((extras_node, extra_ref, extra_value))
                else:
                    self.add((list_value_node, RDF.object, extra_value))

        return extras_node

    def add_record_metadata(self, record):
        """Add the metadata of a record to the RDF graph."""
        record_data = get_record_dict_data(record, self.export_filter, self.user)

        record_ns = Namespace(url_for("records.view_record", id=record.id, _anchor=""))
        self.bind(f"k4m{record.id}", record_ns)

        # Add the basic metadata of the record to the graph.
        record_ref = URIRef(url_for("records.view_record", id=record.id))

        self.add((record_ref, RDF.type, SDO.Dataset))
        self.add((record_ref, SDO.identifier, Literal(record_data["identifier"])))
        self.add((record_ref, SDO.name, Literal(record_data["title"])))
        self.add((record_ref, SDO.text, Literal(record_data["description"])))
        self.add(
            (
                record_ref,
                SDO.dateCreated,
                Literal(record_data["created_at"], datatype=XSD.dateTime),
            )
        )
        self.add(
            (
                record_ref,
                SDO.dateModified,
                Literal(record_data["last_modified"], datatype=XSD.dateTime),
            )
        )

        if record_data["type"] is not None:
            self.add((record_ref, SDO.additionalType, Literal(record_data["type"])))

        for tag in record_data["tags"]:
            self.add((record_ref, SDO.keywords, Literal(tag)))

        if "creator" in record_data:
            author_ref = self.author_ref(record_data["creator"])
            self.add((record_ref, SDO.author, author_ref))

        # Use the license data directly, as only the license name is serialized in the
        # record data.
        if record.license is not None:
            license_id = record.license.url

            # If a license provides no URL, we just use a custom IRI based on the
            # current record.
            if license_id is None:
                license_id = url_for(
                    "records.view_record", id=record.id, _anchor=record.license.name
                )

            self.add((record_ref, SDO.license, URIRef(license_id)))

        # Add the extra metadata of the record to the graph.
        extras_node = self._extras_node(record_data["extras"], record_ns)
        self.add((record_ref, RDFS.isDefinedBy, extras_node))

        # Add the metadata of the record's files to the graph.
        for file_data in record_data["files"]:
            file_ref = URIRef(
                url_for(
                    "records.view_file", record_id=record.id, file_id=file_data["id"]
                )
            )

            self.add((file_ref, RDF.type, SDO.MediaObject))
            self.add((file_ref, SDO.isPartOf, record_ref))
            self.add((file_ref, SDO.identifier, Literal(file_data["id"])))
            self.add((file_ref, SDO.name, Literal(file_data["name"])))
            self.add((file_ref, SDO.text, Literal(file_data["description"])))
            self.add((file_ref, SDO.encodingFormat, Literal(file_data["mimetype"])))
            self.add((file_ref, SDO.contentSize, Literal(str(file_data["size"]))))
            self.add(
                (
                    file_ref,
                    SDO.dateCreated,
                    Literal(file_data["created_at"], datatype=XSD.dateTime),
                )
            )
            self.add(
                (
                    file_ref,
                    SDO.dateModified,
                    Literal(file_data["last_modified"], datatype=XSD.dateTime),
                )
            )

            if "creator" in file_data:
                author_ref = self.author_ref(file_data["creator"])
                self.add((file_ref, SDO.author, author_ref))

        # Add the metadata of the record's links to the graph, if applicable.
        for link_data in record_data.get("links", []):
            record_link_ref = URIRef(
                url_for(
                    "records.view_record_link",
                    record_id=record.id,
                    link_id=link_data["id"],
                )
            )

            self.add((record_link_ref, SDO.name, Literal(link_data["name"])))
            self.add(
                (
                    record_link_ref,
                    SDO.dateCreated,
                    Literal(link_data["created_at"], datatype=XSD.dateTime),
                )
            )
            self.add(
                (
                    record_link_ref,
                    SDO.dateModified,
                    Literal(link_data["last_modified"], datatype=XSD.dateTime),
                )
            )

            if link_data["term"] is not None:
                self.add((record_link_ref, RDF.type, URIRef(link_data["term"])))

            # The outgoing record will always be represented as rdf:subject, the
            # incoming one as rdf:object.
            if "record_from" in link_data:
                from_record_data = link_data["record_from"]
                to_record_data = record_data
            else:
                from_record_data = record_data
                to_record_data = link_data["record_to"]

            self.add(
                (
                    record_link_ref,
                    RDF.subject,
                    URIRef(url_for("records.view_record", id=from_record_data["id"])),
                )
            )
            self.add(
                (
                    record_link_ref,
                    RDF.object,
                    URIRef(url_for("records.view_record", id=to_record_data["id"])),
                )
            )

            if "creator" in link_data:
                author_ref = self.author_ref(link_data["creator"])
                self.add((record_link_ref, SDO.author, author_ref))


class RecordROCrate(ROCrate):
    """Record RO-Crate export class.

    :param record_or_records: A single record or iterable of records to include in the
        RO-Crate.
    :param root_dir: The name of the root directory of the RO-Crate.
    :param export_filter: (optional) See :func:`get_record_export_data`.
    :param user: (optional) The user to check for various access permissions when
        generating the RO-Crate. Defaults to the current user.
    """

    def __init__(self, record_or_records, root_dir, export_filter=None, user=None):
        super().__init__(version="1.0")

        self.root_dir = root_dir
        self.export_filter = export_filter if export_filter is not None else {}
        self.user = user if user is not None else current_user

        if not is_iterable(record_or_records):
            record_or_records = [record_or_records]

        # Collect all the exported data for potential reuse, since they are already
        # required when adding the metadata.
        record_export_data = {}

        # By default, JSON and RDF export data will be added.
        supported_export_types = ["json", "rdf", "pdf"]
        export_types = supported_export_types[:2]

        export_types_filter = self.export_filter.get("export_data")

        if isinstance(export_types_filter, list):
            export_types = [
                export_type
                for export_type in export_types_filter
                if export_type in supported_export_types
            ]

        for record in record_or_records:
            record_export_data[record.id] = {}

            for export_type in export_types:
                args = [record, export_type, self.export_filter, self.user]
                record_export_data[record.id].update(
                    {export_type: get_record_export_data(*args)}
                )

            self.add_record_metadata(record, record_export_data[record.id])

        # Add the actual files to the RO-Crate, if applicable.
        if not self.export_filter.get("metadata_only", False):
            # Add the RO-Crate metadata file.
            arcname = os.path.join(self.root_dir, "ro-crate-metadata.json")
            self.add(self.dump_metadata(), arcname=arcname)

            # Add all record data.
            for record in record_or_records:
                self.add_record_data(record, record_export_data[record.id])

    def _add_author_entity(self, user_data):
        if user_data["orcid"]:
            author_id = f"{const.URL_ORCID}/{user_data['orcid']}"
        else:
            author_id = url_for("accounts.view_user", id=user_data["id"])

        author_entity = self.get_entity(author_id)

        if author_entity is not None:
            return author_entity

        author_entity = {
            "@id": author_id,
            "@type": "Person",
            "identifier": user_data["identity"]["username"],
            "name": user_data["identity"]["displayname"],
        }
        self.root_graph.append(author_entity)

        return author_entity

    def add_record_metadata(self, record, record_export_data):
        """Add the metadata of a record to the RO-Crate."""

        # To collect all file references of a record.
        record_file_references = []

        # Get the serialized record metadata.
        record_data = get_record_dict_data(record, self.export_filter, self.user)
        record_identifier = record_data["identifier"]

        # Collect the record metadata.
        record_entity = {
            "@id": f"./{record_identifier}/",
            "@type": "Dataset",
            "dateCreated": record_data["created_at"],
            "dateModified": record_data["last_modified"],
            "hasPart": record_file_references,
            "identifier": record_data["identifier"],
            "keywords": record_data["tags"],
            "name": record_data["title"],
            "text": record_data["description"],
        }

        if "creator" in record_data:
            author_entity = self._add_author_entity(record_data["creator"])
            record_entity["author"] = {"@id": author_entity["@id"]}

        # Use the license data directly, as only the license name is serialized in the
        # record data.
        if record.license is not None:
            license_id = record.license.url

            # If a license provides no URL, we just use a custom IRI based on the
            # current record.
            if license_id is None:
                license_id = url_for(
                    "records.view_record", id=record.id, _anchor=record.license.name
                )

            record_entity["license"] = {"@id": license_id}

            if self.get_entity(license_id) is None:
                license_entity = {
                    "@id": license_id,
                    "@type": "CreativeWork",
                    "identifier": record.license.name,
                    "name": record.license.title,
                }

                if record.license.url:
                    license_entity["url"] = record.license.url

                self.root_graph.append(license_entity)

        self.root_graph.append(record_entity)

        # Collect the metadata of the record export data.
        for export_type in record_export_data:
            export_meta = const.EXPORT_TYPES["record"][export_type]
            file_id = f"./{record_identifier}/{record_identifier}.{export_meta['ext']}"

            export_entity = {
                "@id": file_id,
                "@type": "File",
                "contentSize": str(record_export_data[export_type].getbuffer().nbytes),
                "dateCreated": utcnow().isoformat(),
                "description": f"{export_meta['title']} export of {record_identifier}.",
                "encodingFormat": mimetypes.guess_type(file_id)[0],
                "name": f"{record_data['identifier']}.{export_meta['ext']}",
            }

            self.root_graph.append(export_entity)
            record_file_references.append({"@id": file_id})

        # Collect the metadata of the record's files.
        for file_data in record_data["files"]:
            # Ensure that the filename always produces valid URIs by quoting it. We also
            # replace slashes beforehand, so we stay consistent with the actual archive
            # names.
            filename = quote(file_data["name"].replace("/", "_"), safe="")
            file_id = f"./{record_identifier}/files/{filename}"

            file_entity = {
                "@id": file_id,
                "@type": "File",
                "contentSize": str(file_data["size"]),
                "dateCreated": file_data["created_at"],
                "dateModified": file_data["last_modified"],
                "encodingFormat": file_data["mimetype"],
                "identifier": file_data["id"],
                "name": file_data["name"],
                "text": file_data["description"],
            }

            if "creator" in file_data:
                author_entity = self._add_author_entity(file_data["creator"])
                file_entity["author"] = {"@id": author_entity["@id"]}

            self.root_graph.append(file_entity)
            record_file_references.append({"@id": file_id})

        self.root_dataset["hasPart"].append({"@id": f"./{record_identifier}/"})

    def add_record_data(self, record, record_export_data):
        """Add the data of a record to the RO-Crate."""

        # Add the record export data.
        for export_type in record_export_data:
            export_meta = const.EXPORT_TYPES["record"][export_type]
            arcname = os.path.join(
                self.root_dir,
                record.identifier,
                f"{record.identifier}.{export_meta['ext']}",
            )

            self.add(record_export_data[export_type], arcname=arcname)

        # Add the record's files.
        for file in record.active_files.order_by(File.last_modified.desc()):
            filepath = file.storage.create_filepath(str(file.id))
            filename = file.name.replace("/", "_")
            arcname = os.path.join(self.root_dir, record.identifier, "files", filename)

            self.add_path(filepath, arcname=arcname)


def filter_extras(extras, excluded_extras):
    """Filter the given extra metadata.

    :param extras: The extras to filter
    :param excluded_extras: A filter mask of extra metadata keys to exclude. See
        :func:`get_record_export_data`.
    :return: A copy of the filtered extras.
    """
    filtered_extras = []

    if not isinstance(excluded_extras, dict):
        excluded_extras = {}

    for index, extra in enumerate(extras):
        filter_key = extra.get("key", str(index))

        # If the dictionary corresponding to the key is empty, the whole extra is
        # excluded.
        if (
            filter_key in excluded_extras
            and isinstance(excluded_extras[filter_key], dict)
            and len(excluded_extras[filter_key]) == 0
        ):
            continue

        new_extra = deepcopy(extra)

        if is_nested_type(extra["type"]):
            new_extra["value"] = filter_extras(
                extra["value"], excluded_extras.get(filter_key)
            )

        filtered_extras.append(new_extra)

    return filtered_extras


def get_record_dict_data(record, export_filter, user):
    """Export a record as a dictionary.

    See :func:`get_record_export_data` for an explanation of the parameters.

    :return: The exported record as a dictionary.
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

    # Collect the basic metadata of the record.
    schema = RecordSchema(exclude=exclude_attrs)
    record_data = schema.dump(record)

    # Exclude any filtered extra metadata.
    excluded_extras = export_filter.get("extras")

    if excluded_extras:
        record_data["extras"] = filter_extras(record_data["extras"], excluded_extras)

    # Include all record files as "files".
    files = record.active_files.order_by(File.last_modified.desc())
    schema = FileSchema(many=True, exclude=exclude_attrs)
    record_data["files"] = schema.dump(files)

    # If not excluded completely, include all, only outgoing or only incoming record
    # links as "links". Only the basic metadata is included for each record, while the
    # current record is always excluded completely, regardless of link direction.
    exclude_links = export_filter.get("links", False)

    if exclude_links is not True:
        direction = None

        if exclude_links == "in":
            direction = "out"
        elif exclude_links == "out":
            direction = "in"

        record_links = get_permitted_record_links(
            record, direction=direction, user=user
        ).order_by(RecordLink.created_at.desc())

        record_data["links"] = []

        for record_link in record_links:
            exclude_record_field = "record_from"
            filter_record_field = "record_to"

            if record_link.record_to_id == record.id:
                exclude_record_field = "record_to"
                filter_record_field = "record_from"

            schema = RecordLinkSchema(
                exclude=[
                    exclude_record_field,
                    *exclude_attrs,
                    *(f"{filter_record_field}.{attr}" for attr in exclude_attrs),
                ]
            )
            link_data = schema.dump(record_link)

            # Exclude any filtered extra metadata in each link as well if propagation is
            # enabled.
            if excluded_extras and export_filter.get("propagate_extras", False):
                link_data[filter_record_field]["extras"] = filter_extras(
                    link_data[filter_record_field]["extras"], excluded_extras
                )

            record_data["links"].append(link_data)

    return record_data


def get_record_json_data(record, export_filter, user):
    """Export a record as a JSON file.

    See :func:`get_record_export_data` for an explanation of the parameters and return
    value.
    """
    record_data = get_record_dict_data(record, export_filter, user)
    json_data = formatted_json(record_data)

    return BytesIO(json_data.encode())


def get_record_pdf_data(record, export_filter, user):
    """Export a record as a PDF file.

    See :func:`get_record_export_data` for an explanation of the parameters and return
        value.
    """
    pdf = RecordPDF(record, export_filter=export_filter, user=user)

    pdf_data = BytesIO()
    pdf.output(pdf_data)
    pdf_data.seek(0)

    return pdf_data


def get_record_qr_data(record):
    """Export a record as a QR code in PNG format.

    See :func:`get_record_export_data` for an explanation of the parameters and return
        value.
    """
    image = qrcode.make(url_for("records.view_record", id=record.id))

    image_data = BytesIO()
    image.save(image_data, format="PNG")
    image_data.seek(0)

    return image_data


def get_record_rdf_data(record, export_filter, user):
    """Export a record as an RDF graph in Turtle format.

    See :func:`get_export_data` for an explanation of the parameters and return value.
    """
    rdf_graph = RecordRDFGraph(record, export_filter=export_filter, user=user)

    try:
        rdf_data = rdf_graph.serialize(format="turtle")
    except:
        # Just in case, even if all IRIs should be valid.
        rdf_data = ""

    return BytesIO(rdf_data.encode())


def get_record_ro_crate_data(record, export_filter, user):
    """Export a record as an RO-Crate.

    See :func:`get_record_export_data` for an explanation of the parameters and return
    value.
    """
    ro_crate = RecordROCrate(
        record, record.identifier, export_filter=export_filter, user=user
    )

    if export_filter.get("metadata_only", False):
        return BytesIO(ro_crate.dump_metadata().encode())

    return ro_crate


def get_record_export_data(record, export_type, export_filter=None, user=None):
    """Export a record in a given format.

    :param record: The record to export.
    :param export_type: The export type, one of ``"json"``, ``"rdf"``, ``"pdf"``,
        ``"qr"`` or ``"ro-crate"``.
    :param export_filter: (optional) A dictionary specifying various filters to adjust
        the returned export data, depending on the export type. Currently only usable in
        combination with the ``"json"``, ``"rdf"``, ``"pdf"`` and ``"ro-crate"`` export
        types. Note that the values in the example below represent the respective
        default values.

        **Example:**

        .. code-block:: python3

            {
                # Whether user information about the creator of the record or any linked
                # resource should be excluded.
                "user": False,
                # Whether to exclude all (True), outgoing ("out") or incoming ("in")
                # links of the record with other records.
                "links": False,
                # A dictionary specifying a filter mask of extra metadata keys to
                # exclude, e.g. {"sample_key": {}, "sample_list": {"0": {}}}. The value
                # of each key can either be an empty dictionary, to exclude the whole
                # extra, or another dictionary with the same possibilities as in the
                # parent dictionary. For list entries, indices need to be specified as
                # strings, starting at 0.
                "extras": {},
                # Whether to apply the extras filter mask to any linked records as well.
                "propagate_extras": False,
                # To specify which kind of export data of records should be included in
                # an exported RO-Crate when using the "ro-crate" export type. All other
                # filters also apply to this export data, as far as applicable.
                "export_data": ["json", "rdf"],
                # Whether to return only the metadata file of an exported RO-Crate when
                # using the "ro-crate" export type.
                "metadata_only": False,
            }

    :param user: (optional) The user to check for various access permissions when
        generating the export data. Defaults to the current user.
    :return: The exported record data as an in-memory byte stream or ``None`` if an
        unknown export type was given. Note that for the ``ro-crate`` export type, the
        returned data is an iterable producing the actual data on the fly instead,
        unless only the metadata file is exported by specifying the corresponding export
        filter.
    """
    export_filter = export_filter if export_filter is not None else {}
    user = user if user is not None else current_user

    if export_type == "json":
        return get_record_json_data(record, export_filter, user)

    if export_type == "pdf":
        return get_record_pdf_data(record, export_filter, user)

    if export_type == "qr":
        return get_record_qr_data(record)

    if export_type == "rdf":
        return get_record_rdf_data(record, export_filter, user)

    if export_type == "ro-crate":
        return get_record_ro_crate_data(record, export_filter, user)

    return None


def _to_plain_format(extras, nested_type=None):
    if nested_type == "list":
        converted_extras = []
    else:
        converted_extras = {}

    for extra in extras:
        if is_nested_type(extra["type"]):
            value = _to_plain_format(extra["value"], nested_type=extra["type"])
        else:
            value = extra["value"]

        if nested_type == "list":
            converted_extras.append(value)
        else:
            converted_extras[extra["key"]] = value

    return converted_extras


def get_extras_json_data(record, export_filter):
    """Export the extras of a record as a JSON file.

    See :func:`get_extras_export_data` for an explanation of the parameters and return
    value.
    """
    extras = record.extras
    excluded_extras = export_filter.get("extras")

    if excluded_extras:
        extras = filter_extras(extras, excluded_extras)

    if export_filter.get("format") == "plain":
        extras = _to_plain_format(extras)

    json_data = formatted_json(extras)
    return BytesIO(json_data.encode())


def get_extras_export_data(record, export_type, export_filter=None):
    """Export the extras of a record in a given format.

    :param record: The record whose extras should be exported.
    :param export_type: The export type, currently only ``"json"``.
    :param export_filter: (optional) A dictionary specifying various filters to adjust
        the returned export data. Note that the values in the example below represent
        the respective default values.

        **Example:**

        .. code-block:: python3

            {
                # A dictionary specifying a filter mask of extra metadata keys to
                # exclude, e.g. {"sample_key": {}, "sample_list": {"0": {}}}. The value
                # of each key can either be an empty dictionary, to exclude the whole
                # extra, or another dictionary with the same possibilities as in the
                # parent dictionary. For list entries, indices need to be specified as
                # strings, starting at 0.
                "extras": {},
                # The format of an exported JSON file when using the "json" export type.
                # This can either be the regular format used by Kadi4Mat ("standard") or
                # a simplified format, mapping keys directly to their respective values
                # ("plain").
                "format": "standard",
            }

    :return: The exported record data as an in-memory byte stream or ``None`` if an
        unknown export type was given.
    """
    export_filter = export_filter if export_filter is not None else {}

    if export_type == "json":
        return get_extras_json_data(record, export_filter)

    return None
