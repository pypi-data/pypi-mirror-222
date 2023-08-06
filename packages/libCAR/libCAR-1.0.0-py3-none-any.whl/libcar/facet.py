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

import typing as t
import construct as cs

from construct_dataclasses import (
    csfield,
    subcsfield,
    to_struct,
    dataclass_struct,
)

from libcar.bom import BOM
from libcar.keys import CAR_FACET_KEYS_VARIABLE
from libcar.attr import CARAttributePair

@dataclass_struct
class CARFacetValue:
    # ????
    unknown_1: int = csfield(cs.Int16ul)
    unknown_2: int = csfield(cs.Int16ul)

    attributes_count: int = csfield(cs.Int16ul)
    attributes: list[CARAttributePair] = subcsfield(
        CARAttributePair,
        cs.Array(cs.this.attributes_count, to_struct(CARAttributePair)),
    )

class it_facets:
    def __init__(self, bom: BOM) -> None:
        self.bom = bom

    def __iter__(self) -> t.Generator[tuple[str, CARFacetValue], t.Any, None]:
        tree = self.bom.tree_of(CAR_FACET_KEYS_VARIABLE)
        # The key will be always an encoded string
        for key, value in self.bom.iter_tree(tree):
            yield key.decode(), CARFacetValue.parser.parse(value)

