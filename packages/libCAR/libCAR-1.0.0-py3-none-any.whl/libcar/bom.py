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

from construct_dataclasses import csfield, subcsfield, to_struct, dataclass_struct

# =============================================================================
# Excerpt from archived Facebook Github repository at facebookarchive/xcbuild.
#
# Copyright (c) 2015-present, Facebook, Inc.
# All rights reserved.
# Build of Materials format (BOM)
#
# BOM files are a nonstandard archive format originating in NeXTSTEP and
# since used in OS X package installers and compiled asset archives.
#
# The structure of a BOM file is simple, with three major file sections
# described by a header at the start of the file. Most fields stored in
# BOM files are big endian.
#
# The first section of a BOM file is the index. This contains a list of
# file offsets into the data section and a length, identified by index.
# The BOM index is used for both data in the BOM format itself, as well
# as for contents within the data section to refer to other data. After
# the index list is the free list, which presumably lists available data
# segments that can be filled by later index insertions.
#
# The next section is the variables. BOM variables have a name and an
# index into the index section pointing to the variable's data.
#
# Finally, the data section contains the data pointed to by the BOM index.
# =============================================================================

BOM_HEADER_MAGIC = b"BOMStore"


@dataclass_struct
class BOMHeader:
    magic: bytes = csfield(cs.Const(BOM_HEADER_MAGIC))
    version: int = csfield(cs.Int32ub)
    block_count: int = csfield(cs.Int32ub)
    index_offset: int = csfield(cs.Int32ub)  # Length of first part
    index_length: int = csfield(cs.Int32ub)  # Length of the second part
    variables_offset: int = csfield(cs.Int32ub)
    trailer_len: int = csfield(cs.Int32ub)


@dataclass_struct
class BOMIndex:
    address: int = csfield(cs.Int32ub)
    length: int = csfield(cs.Int32ub)


@dataclass_struct
class BOMIndexHeader:
    count: int = csfield(cs.Int32ub)
    items: list[BOMIndex] = subcsfield(
        BOMIndex, cs.Array(cs.this.count, to_struct(BOMIndex))
    )


@dataclass_struct
class BOMVariable:
    index: int = csfield(cs.Int32ub)
    length: int = csfield(cs.Int8ub)
    name: bytes = csfield(cs.PaddedString(cs.this.length, "utf-8"))


@dataclass_struct
class BOMVariables:
    count: int = csfield(cs.Int32ub)
    variables: list[BOMVariable] = subcsfield(
        BOMVariable, cs.Array(cs.this.count, to_struct(BOMVariable))
    )

    def get(self, name: bytes, __default=None) -> BOMVariable:
        for variable in self.variables:
            if variable.name == name:
                return variable
        return __default


@dataclass_struct
class BOMTree:
    magic: bytes = csfield(cs.Const(b"tree"))
    version: int = csfield(cs.Int32ub)
    child: int = csfield(cs.Int32ub)  # index of BOMIndex in BOMIndexHeader.items
    node_size: int = csfield(cs.Int32ub)
    path_count: int = csfield(cs.Int32ub)
    unknown: int = csfield(cs.Int8ub)


@dataclass_struct
class BOMTreeEntryIndex:
    value_index: int = csfield(cs.Int32ub)
    key_index: int = csfield(cs.Int32ub)


@dataclass_struct
class BOMTreeEntry:
    # if 0 then this entry refers to other BOMPaths entries
    is_leaf: int = csfield(cs.Int16ub)
    #  for leaf, count of paths. for top level, (# of leafs - 1)
    count: int = csfield(cs.Int16ub)
    forward: int = csfield(cs.Int32ub)  #  next leaf, when there are multiple leafs
    backward: int = csfield(cs.Int32ub)  # previous leaf, when there are multiple leafs
    indexes: list[BOMTreeEntryIndex] = subcsfield(
        BOMTreeEntryIndex, cs.Array(cs.this.count, to_struct(BOMTreeEntryIndex))
    )


class BOM:
    def __init__(self, fp: io.IOBase) -> None:
        # NOTE: the stream must be seekable, so that we can change our
        # position dynamically
        self.stream = fp
        self._head = BOMHeader.parser.parse_stream(fp)
        # Next, we have to parse the variables and index objects
        fp.seek(self.header.variables_offset, 0)
        self._vars = BOMVariables.parser.parse_stream(fp)
        fp.seek(self.header.index_offset, 0)
        self._index = BOMIndexHeader.parser.parse_stream(fp)

    @property
    def header(self) -> BOMHeader:
        return self._head

    @property
    def variables(self) -> BOMVariables:
        return self._vars

    @property
    def index_header(self) -> BOMIndexHeader:
        return self._index

    def index_of(self, name: bytes) -> BOMIndex:
        variable = self.variables.get(name)
        if not variable:
            raise ValueError(f"Could not find variable {name}")

        return self.get_index(variable.index)

    def get_index(self, pos: int) -> BOMIndex:
        return self.index_header.items[pos]

    def tree_of(self, name: bytes) -> BOMTree:
        index = self.index_of(name)
        return self.get_tree(index)

    def get_tree(self, index: BOMIndex) -> BOMTree:
        self.stream.seek(index.address)
        return BOMTree.parser.parse_stream(self.stream)

    def get_tree_entry(self, tree: BOMTree) -> BOMTreeEntry:
        index = self.get_index(tree.child)
        self.stream.seek(index.address, 0)
        return BOMTreeEntry.parser.parse_stream(self.stream)

    def read(self, index: BOMIndex) -> bytes:
        self.stream.seek(index.address, 0)
        return self.stream.read(index.length)

    def iter_tree(self, tree: BOMTree) -> t.Generator[tuple[bytes, bytes], t.Any, None]:
        entry = self.get_tree_entry(tree)
        if not entry.is_leaf:
            index = entry.indexes[0]
            self.stream.seek(self.get_index(index.value_index).address, 0)
            entry = BOMTreeEntry.parser.parse_stream(self.stream)

        while entry:
            for index in entry.indexes:
                key_item = self.get_index(index.key_index)
                value_item = self.get_index(index.value_index)

                # The key is an encoded string, so we can read it directly
                key = self.read(key_item)
                value = self.read(value_item)  # not sure if this is safe
                yield key, value

            if not entry.forward:
                break
            # Forward to next tree entry
            index = self.get_index(entry.forward)
            self.stream.seek(index.address, 0)
            entry = BOMTreeEntry.parser.parse_stream(self.stream)
