# Copyright (C) 2023 MatrixEditor

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

import io
import typing as t
import construct as cs
import enum

from libcar.bom import BOM
from libcar import keys, attr
from libcar.facet import it_facets
from libcar.rendition import it_renditions

from construct_dataclasses import (
    csfield,
    dataclass_struct,
    tfield,
)

# =============================================================================
# Excerpt from archived Facebook Github repository at facebookarchive/xcbuild.
#
# Copyright (c) 2015-present, Facebook, Inc.
# All rights reserved.
#
#  Compiled Asset Archive format (car)
#
# A car file is a BOM file with a number of special variables. Conceptually, a
# car file contains a set of "facets", or named assets, and "renditions", or
# specific variants of those assets based on a variety of parameters. It also
# supports a number of other types of content which aren't supported/described.
#
# The highest level variable in a car file is the CARHEADER, which has some
# metadata about the file contents, a version marker, and creator string. This
# is stored as a custom structure.
#
# The next level is the list of facets, stored in FACETKEYS as a standard BOM
# tree. In the tree, the leaf keys are the facet's name (stored as a string)
# and the values are a list of attribute key-value pairs. Of those attributes,
# the `identifier` key is used to find the renditions comprising the facet.
#
# The KEYFORMAT variable describes the order of keys used to identify renditions,
# also in a simple custom structure format.
#
# Renditions are listed in the RENDITIONS variable in a BOM tree. The keys of
# the tree hold a list of attribute values, matching the order of attribute
# identifiers in the KEYFORMAT variable. Each rendition key is unique and has
# an identifier connecting it to the facet it beongs to.
#
# Rendition values are a custom structure format with a number of pieces. The
# first is the rendition header, which has metadata about the rendition like
# its original file name, width, height, scale, and pixel format. Following
# that is the information list, a variable length section describing properties
# applying to only certain images, like slicing and format details.
#
# Directly after the info section is the image data. This is found in one of
# three formats, preceded by a header specifying the data length:
#
#  1. Direct gzip image data. The image data matches the pixel format noted
#     in the rendition header.
#  2. LZVN compressed image data. LZVN is a custom compression algorithm that
#     is also (apparently) used for compressing OS X kernel images.
#  3. A sub-header is sometimes present, usually followed by LZVN data. The
#     purpose of this sub-header is unclear.
# =============================================================================


# -- Enums -------------------------------------------------------------------
class ColorSpace(enum.IntEnum):
    SRGB = 0
    GrayGamma2_2 = 1
    DisplayP3 = 2
    ExtendedRangeSRGB = 3
    ExtendedLinearSRGB = 4
    ExtendedGray = 5


# -- Structs -----------------------------------------------------------------
@dataclass_struct
class CARHeader:
    magic: int = csfield(cs.Const(b"RATC"))
    ui_version: int = csfield(cs.Int32ul)
    storage_version: int = csfield(cs.Int32ul)
    storage_timestamp: int = csfield(cs.Int32ul)
    rendition_count: int = csfield(cs.Int32ul)
    file_creator: bytes = csfield(cs.PaddedString(128, "utf-8"))
    other_creator: bytes = csfield(cs.PaddedString(256, "utf-8"))
    uuid: bytes = csfield(cs.Bytes(16))
    checksum: int = csfield(cs.Int32ul)  # crc32?
    schema_version: int = csfield(cs.Int32ul)
    color_space_id: ColorSpace = tfield(
        ColorSpace, cs.Enum(cs.Int32ul, ColorSpace)
    )
    key_semantics: int = csfield(cs.Int32ul)


@dataclass_struct
class CARExtendedMetadata:
    magic: bytes = csfield(cs.Const(b"META"))
    thinning_args: str = csfield(cs.PaddedString(256, "utf-8"))
    platform_version: str = csfield(cs.PaddedString(256, "utf-8"))
    platform: str = csfield(cs.PaddedString(256, "utf-8"))
    authoring_tool: str = csfield(cs.PaddedString(256, "utf-8"))


@dataclass_struct
class CARKeyFormat:
    magic: bytes = csfield(cs.Const(b"tmfk"))
    reserved: int = csfield(cs.Int32ul)
    id_count: int = csfield(cs.Int32ul)
    identifiers: list[attr.Identifier] = tfield(
        attr.Identifier,
        cs.Array(cs.this.id_count, cs.Enum(cs.Int32ul, attr.Identifier)),
    )


# -- Classes -----------------------------------------------------------------
class it_appearance_keys:
    def __init__(self, bom: BOM) -> None:
        self.bom = bom

    def __iter__(self) -> t.Generator[tuple[str, int], t.Any, None]:
        tree = self.bom.tree_of(keys.CAR_APPEARANCE_KEYS)
        for key, value in self.bom.iter_tree(tree):
            yield key.decode(), cs.Int16ul.parse(value)


class CAR:
    def __init__(self, bom: BOM) -> None:
        # No action just yet: all objects will be parsed within their method call
        self.bom = bom

    @staticmethod
    def parse(data: bytes) -> CAR:
        return CAR.parse_stream(io.BytesIO(data))

    @staticmethod
    def parse_file(path: str) -> CAR:
        with open(path, "rb") as fp:
            return CAR.parse(fp.read())

    @staticmethod
    def parse_stream(stream: io.IOBase) -> CAR:
        bom = BOM(stream)
        return CAR(bom)

    @property
    def stream(self) -> io.IOBase:
        return self.bom.stream

    @property
    def key_format(self) -> CARKeyFormat:
        self._seek(keys.CAR_KEY_FORMAT_VARIABLE)
        return CARKeyFormat.parser.parse_stream(self.stream)

    @property
    def header(self) -> CARHeader:
        self._seek(keys.CAR_HEADER_VARIABLE)
        return CARHeader.parser.parse_stream(self.stream)

    @property
    def metadata(self) -> CARExtendedMetadata:
        self._seek(keys.CAR_EXTENDED_METADATA_VARIABLE)
        return CARExtendedMetadata.parser.parse_stream(self.stream)

    @property
    def facets(self) -> it_facets:
        return it_facets(self.bom)

    def iter_renditions(self, key_format: CARKeyFormat = None) -> it_renditions:
        if key_format is None:
            key_format = self.key_format

        return it_renditions(self.bom, key_format)

    def iter_tree(self, name: str) -> t.Generator[tuple[bytes, bytes], t.Any, None]:
        tree = self.bom.tree_of(name)
        return self.bom.iter_tree(tree)

    @property
    def appearance_keys(self) -> it_appearance_keys:
        return it_appearance_keys(self.bom)

    # -- internal methods --
    def _seek(self, var_name: bytes) -> None:
        index = self.bom.index_of(var_name)
        self.stream.seek(index.address, 0)
