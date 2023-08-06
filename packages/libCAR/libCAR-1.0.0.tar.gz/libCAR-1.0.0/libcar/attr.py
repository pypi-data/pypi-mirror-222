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

import enum
import construct as cs

from construct_dataclasses import (
    csfield,
    dataclass_struct,
    tfield,
)


class Identifier(enum.IntEnum):
    look = 0
    element = 1
    part = 2
    size = 3
    direction = 4
    place_holder = 5
    value = 6
    appearance = 7
    dimension1 = 8
    dimension2 = 9
    state = 10
    layer = 11
    scale = 12
    unknown_13 = 13
    presentation_state = 14
    idiom = 15
    subtype = 16
    identifier = 17
    previous_value = 18
    previous_state = 19
    size_class_horizontal = 20
    size_class_vertical = 21
    memory_class = 22
    graphics_class = 23
    display_gamut = 24
    deployment_target = 25

    # Not a real value; used as a marker for the maximum identifier.
    _count = 26


class SizeValue(enum.IntEnum):
    regular = 0
    small = 1
    mini = 2
    large = 3


class DirectionValue(enum.IntEnum):
    horizontal = 0
    vertical = 1
    pointing_up = 2
    pointing_down = 3
    pointing_left = 4
    pointing_right = 5


class ValueValue(enum.IntEnum):
    off = 0
    on = 1
    mixed = 2


class StateValue(enum.IntEnum):
    normal = 0
    rollover = 1
    pressed = 2
    obsolete_inactive = 3
    disabled = 4
    deeply_pressed = 5


class LayerValue(enum.IntEnum):
    base = 0
    highlight = 1
    mask = 2
    pulse = 3
    hit_mask = 4
    pattern_overlay = 5
    outline = 6
    interior = 7


class PresentationStateValue(enum.IntEnum):
    active = 0
    inactive = 1
    active_main = 2


class IdiomValue(enum.IntEnum):
    universal = 0
    phone = 1
    pad = 2
    tv = 3
    car = 4
    watch = 5
    marketing = 6


class SizeClassValue(enum.IntEnum):
    unspecified = 0
    compact = 1
    regular = 2

@dataclass_struct
class CARAttributePair:
    identifier: Identifier = tfield(
        Identifier, cs.Enum(cs.Int16ul, Identifier)
    )
    value: int = csfield(cs.Int16ul)
