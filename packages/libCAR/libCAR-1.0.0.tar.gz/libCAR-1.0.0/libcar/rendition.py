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
import enum
import typing as t
import construct as cs

from dataclasses import dataclass
from construct_dataclasses import (
    csfield,
    subcsfield,
    to_struct,
    dataclass_struct,
    tfield,
)


from libcar.bom import BOM
from libcar.keys import CAR_RENDITIONS_VARIABLE
from libcar.attr import IdiomValue

# -- Constants ---------------------------------------------------------------

COLOR_DATA_MAGIC = b"RLOC"  # COLR
RAW_DATA_MAGIC = b"DWAR"  # RAWD
THEME_DATA_MAGIC = b"MLEC"  # CELM ??
MIMAGE_SET_DATA_MAGIC = b"SISM"  # MSIS (MultiSize Image Set)

# -- Enums -------------------------------------------------------------------


class Magic(enum.IntEnum):
    slices = 1001
    metrics = 1003
    composition = 1004
    uti = 1005
    bitmap_info = 1006
    bytes_per_row = 1007
    reference = 1010
    alpha_cropped_frame = 1011


class PixelFormat(enum.Enum):
    ARGB = b"BGRA"  # color + alpha
    GA8 = b" 8AG"  # gray + alpha
    GA16 = b"61AG"  # gray + alpha
    RGB5 = b"5BGR"  # color (5bit)
    RGBW = b"WBGR"  # rgb + white light
    PDF = b" FDP"  # pdf document
    RAW_DATA = b"ATAD"  # raw data
    JPEG = b"GPEJ"  # jpeg image
    NON_STANDARD_WEBP = b"PBEW"  # webp image
    SVG = b" GVS"  # svg image
    HEIF = b"FIEH"  # ??

    @staticmethod
    def is_saved_as_raw_data(pixel_format: bytes) -> bool:
        return pixel_format in (
            PixelFormat.JPEG.value,
            PixelFormat.PDF.value,
            PixelFormat.RAW_DATA.value,
            PixelFormat.NON_STANDARD_WEBP.value,
            PixelFormat.SVG.value,
        )


class Layout(enum.IntEnum):
    gradient = 6
    effect = 7
    vector = 9
    one_part_fixed_size = 10
    one_part_tile = 11
    one_part_scale = 12
    three_part_horizontal_tile = 20
    three_part_horizontal_scale = 21
    three_part_horizontal_uniform = 22
    three_part_vertical_tile = 23
    three_part_vertical_scale = 24
    three_part_vertical_uniform = 25
    nine_part_tile = 30
    nine_part_scale = 31
    nine_part_horizontal_uniform_vertical_scale = 32
    nine_part_horizontal_scale_vertical_uniform = 33
    nine_part_edges_only = 34
    six_part = 40
    animation_filmstrip = 50

    # Non-images > 999:
    raw_data = 1000
    external_link = 1001
    layer_stack = 1002
    internal_link = 1003
    asset_pack = 1004
    name_list = 1005
    texture = 1007
    texture_image = 1008
    color = 1009
    multisize_image = 1010
    layer_reference = 1011
    content_rendition = 1012
    recognition_object = 1013


class CompressionMagic(enum.IntEnum):
    UNCOMPRESSED = 0
    RLE = 1
    ZIP = 2  # zlib
    LZVN = 3
    LZFSE = 4
    JPEG_LZFSE = 5
    BLURREDIMAGE = 5
    ASTC = 6
    PALETTE_IMG = 8
    HEVC = 9
    DEEPMAP_LZFSE = 10
    DEEPMAP2 = 11

class DeepMap2Type(enum.IntEnum):
    NONE = 1
    DefaultScratchBufferSize = 2
    LosslessScratchBufferSize = 3
    PaletteScratchBufferSize = 4

# -- Structs -----------------------------------------------------------------


@dataclass_struct
class CARRenditionInfoSlice:
    x: int = csfield(cs.Int32ul)
    y: int = csfield(cs.Int32ul)
    width: int = csfield(cs.Int32ul)
    height: int = csfield(cs.Int32ul)


@dataclass_struct
class CARRenditionInfoSlices:
    nslices: int = csfield(cs.Int32ul)
    slices: list[CARRenditionInfoSlice] = subcsfield(
        CARRenditionInfoSlice,
        cs.Array(cs.this.nslices, to_struct(CARRenditionInfoSlice)),
    )


@dataclass_struct
class CARRenditionInfoMetric:
    width: int = csfield(cs.Int32ul)
    height: int = csfield(cs.Int32ul)


@dataclass_struct
class CARRenditionInfoMetrics:
    metrics_count: int = csfield(cs.Int32ul)
    top_right_inset: CARRenditionInfoMetric = csfield(CARRenditionInfoMetric)
    bottom_left_inset: CARRenditionInfoMetric = csfield(CARRenditionInfoMetric)
    image_size: CARRenditionInfoMetric = csfield(CARRenditionInfoMetric)


@dataclass_struct
class CARRenditionInfoComposition:
    blend_mode: int = csfield(cs.Int32ul)
    opacity: float = csfield(cs.Float32l)


@dataclass_struct
class CARRenditionInfoUti:
    uti_length: int = csfield(cs.Int32ul)
    uti: bytes = csfield(cs.Bytes(cs.this.uti_length))


@dataclass_struct
class CARRenditionInfoBitmapInfo:
    exif_orientation: int = csfield(cs.Int32ul)


@dataclass_struct
class CARRenditionInfoBytesPerRow:
    bytes_per_row: int = csfield(cs.Int32ul)


@dataclass_struct
class CARRenditionInfoReference:
    magic: bytes = csfield(cs.Const(b"KLNI"))  # maybe switch to constant
    padding: int = csfield(cs.Int32ul)  # always 0?
    x: int = csfield(cs.Int32ul)
    y: int = csfield(cs.Int32ul)
    width: int = csfield(cs.Int32ul)
    height: int = csfield(cs.Int32ul)
    # layout: since rendition header says internal link
    layout: Layout = csfield(cs.Enum(cs.Int16ul, Layout))
    key_length: int = csfield(cs.Int32ul)  # rendition containing data
    key: bytes = csfield(cs.Bytes(cs.this.key_length))


@dataclass_struct
class CARRenditionThemeCBCK:  # together with
    magic: bytes = csfield(cs.Const(b"KCBC"))
    unknown_1: int = csfield(cs.Int32ul)
    unknown_2: int = csfield(cs.Int32ul)
    unknown_3: int = csfield(cs.Int32ul)


@dataclass_struct
class CARRenditionRawData:
    magic: bytes = csfield(cs.Const(b"DWAR"))  # RAWD
    # 0: not compressed, 1: compressed using lzfse
    compressed: int = csfield(cs.Int32ul)
    length: int = csfield(cs.Int32ul)
    data: bytes = csfield(cs.Bytes(cs.this.length))


@dataclass_struct
class CARRenditionColor:
    magic: bytes = csfield(cs.Const(b"RLOC"))  # COLR
    version: int = csfield(cs.Int32ul)
    flags: int = csfield(cs.Int32ul)
    comp_count: int = csfield(cs.Int32ul)
    components: list[float] = csfield(cs.Array(cs.this.comp_count, cs.Double))


@dataclass_struct
class CARMultisizeImageSetEntry:
    width: int = csfield(cs.Int32ul)
    height: int = csfield(cs.Int32ul)
    index: int = csfield(cs.Int16ul)
    idiom: IdiomValue = tfield(IdiomValue, cs.Enum(cs.Int16ul, IdiomValue))


@dataclass_struct
class CARMultisizeImageSet:
    magic: bytes = csfield(cs.Const(b"SISM"))  # MSIS
    version: int = csfield(cs.Int32ul)
    sizes_count: int = csfield(cs.Int32ul)
    entries: list[CARMultisizeImageSetEntry] = subcsfield(
        CARMultisizeImageSetEntry,
        cs.Array(cs.this.sizes_count, CARMultisizeImageSetEntry.struct),
    )


@dataclass_struct
class CARRenditionUnknown:
    magic: bytes = csfield(cs.Bytes(4))  # RAWD
    version: int = csfield(cs.Int32ul)
    length: int = csfield(cs.Int32ul)
    data: bytes = csfield(cs.Bytes(cs.this.length))


@dataclass_struct
class CARRenditionDeepMap2Data:
    magic: bytes = csfield(cs.Const(b"dmp2"))
    block_count: int = csfield(cs.Int8ul)
    unknown_1: int = csfield(cs.Int8ul)
    unknown_2: int = csfield(cs.Int8ul)
    type: DeepMap2Type = tfield(DeepMap2Type, cs.Enum(cs.Int8ul, DeepMap2Type))
    width: int = csfield(cs.Int16ul)
    height: int = csfield(cs.Int16ul)
    size: int = csfield(cs.Int32ul)
    payload: bytes | None = csfield(cs.Optional(cs.Bytes(cs.this.size)))


@dataclass_struct
class CARRenditionDeepMap2:
    version: int = csfield(cs.Int32ul) # always 1
    encoding: CompressionMagic = tfield(
        CompressionMagic, cs.Enum(cs.Int32ul, CompressionMagic)
    )
    data_size: int = csfield(cs.Int32ul)
    reserved: int = csfield(cs.Int32ul) # always 0
    data: CARRenditionDeepMap2Data = csfield(CARRenditionDeepMap2Data)



# -- Classes -----------------------------------------------------------------
@dataclass
class RenditionValueData:
    headers: list[CARRenditionInfoHeader]
    # Marked as unknown by default, but can take the following types:
    #   - CARRenditionRawData
    #   - CARRenditionTheme
    #   - CARMultisizeImageSet
    #   - CARRenditionColor
    value: CARRenditionUnknown


# -- Adapters -----------------------------------------------------------------
class RenditionInfoHeaderAdapter(cs.Adapter):
    def __init__(self) -> None:
        super().__init__(cs.Bytes(cs.this.length))

    def _encode(self, obj: t.Any, context: cs.Context, path: cs.PathType) -> t.Any:
        # As the object will always be a dataclass struct, we can use
        # its static parser instance.
        return obj.__class__.parser.build(obj)

    def _decode(self, data: bytes, context: cs.Context, path: cs.PathType) -> t.Any:
        # The magic value tells us what structure we have to parse
        if isinstance(context.magic, cs.EnumIntegerString):
            magic = context.magic.intvalue
        else:
            magic = context.magic

        dc_struct = None
        if magic == Magic.uti:
            dc_struct = CARRenditionInfoUti
        elif magic == Magic.slices:
            dc_struct = CARRenditionInfoSlices
        elif magic == Magic.metrics:
            dc_struct = CARRenditionInfoMetrics
        elif magic == Magic.bitmap_info:
            dc_struct = CARRenditionInfoBitmapInfo
        elif magic == Magic.bytes_per_row:
            dc_struct = CARRenditionInfoBytesPerRow
        elif magic == Magic.reference:
            dc_struct = CARRenditionInfoReference
        elif magic == Magic.composition:
            dc_struct = CARRenditionInfoComposition
        else:
            # _ raise ValueError(f"Unknown/Unsupported type: {magic:#x}")
            return data

        return dc_struct.parser.parse(data)


@dataclass_struct
class CARRenditionInfoHeader:
    # NOTE: this magic indicates how the field should be treated.
    magic: Magic = tfield(Magic, cs.Enum(cs.Int32ul, Magic))
    length: int = csfield(cs.Int32ul)
    # The type of the content field will be one of the following:
    #  - CARRenditionInfoUti
    #  - CARRenditionInfoSlices
    #  - CARRenditionInfoMetrics
    #  - CARRenditionInfoBitmapInfo
    #  - CARRenditionInfoBytesPerRow
    #  - CARRenditionInfoReference
    #  - CARRenditionInfoComposition
    #
    # NOTE: the content will still remain bytes if no parser
    # is implemented for the requested type!
    content: t.Any | bytes = csfield(RenditionInfoHeaderAdapter())


class RenditionAdapter(cs.Adapter):
    def _encode(
        self, obj: RenditionValueData, context: cs.Context, path: cs.PathType
    ) -> t.Any:
        # The headers will be put together with a join(...) call and
        # the parsed data uses its parser instance to build
        payload = b"".join(map(lambda x: x.parser.build(x), obj.headers))
        return payload + obj.value.parser.build(obj.value)

    def _decode(self, data: bytes, context: cs.Context, path: cs.PathType) -> t.Any:
        # 1. Step: extract all info headers
        headers = []
        stream = io.BytesIO(data[: context.info_len])
        offset = 0
        while offset < context.info_len:
            stream.seek(offset, 0)
            header = CARRenditionInfoHeader.parser.parse_stream(stream)
            # Just add the header at the end of our list, don't do anything else
            # with it just yet.
            headers.append(header)
            offset += header.length + (cs.Int32ul.sizeof() * 2)

        stream.close()
        # 2. Parse rendition payloads [if available]
        if context.payload_size == 0:
            return RenditionValueData(headers, None)

        stream = io.BytesIO(data[context.info_len :])
        magic = stream.read(4)
        dc_struct = None
        if magic == THEME_DATA_MAGIC:
            dc_struct = CARRenditionTheme
        elif magic == COLOR_DATA_MAGIC:
            dc_struct = CARRenditionColor
        elif magic == RAW_DATA_MAGIC:
            dc_struct = CARRenditionRawData
        elif magic == MIMAGE_SET_DATA_MAGIC:
            dc_struct = CARMultisizeImageSet

        # Validate if we have a valid struct
        if dc_struct is None:
            dc_struct = CARRenditionUnknown

        payload = dc_struct.parser.parse(data[context.info_len :])
        return RenditionValueData(headers, payload)


@dataclass_struct
class CARRenditionValue:
    # swapped CTSI: Core Theme Structured Image
    magic: bytes = csfield(cs.Const(b"ISTC"))
    version: int = csfield(cs.Int32ul)
    flags: int = csfield(cs.Int32ul)
    width: int = csfield(cs.Int32ul)
    height: int = csfield(cs.Int32ul)
    scale_factor: int = csfield(cs.Int32ul)  # scale100. 100 is 1x, 200 is 2x, etc.
    pixel_format: bytes = csfield(cs.Bytes(4))
    color_space_id: int = csfield(cs.Int8ul)
    reserved_1: bytes = csfield(cs.Bytes(3))

    # modification date in seconds since 1970?
    modification_date: int = csfield(cs.Int32ul)
    # layout/type of the rendition
    layout: int | Layout = tfield(Layout, cs.Enum(cs.Int16ul, Layout))
    reserved_2: int = csfield(cs.Int16ul)
    name: bytes = csfield(cs.PaddedString(128, "utf-8"))

    # size of the list of information after header but before bitmap
    info_len: int = csfield(cs.Int32ul)

    bitmap_count: int = csfield(cs.Int32ul)
    reserved_3: int = csfield(cs.Int32ul)
    # size of all the proceeding information info_len + data
    payload_size: int = csfield(cs.Int32ul)
    data: RenditionValueData = csfield(
        RenditionAdapter(cs.Bytes(cs.this.payload_size + cs.this.info_len))
    )

class ThemeRenditionAdapter(cs.Adapter):
    def __init__(self) -> None:
        super().__init__(cs.Bytes(cs.this.length))

    def _encode(self, obj: bytes | CARRenditionDeepMap2, context: cs.Context, path: cs.PathType) -> t.Any:
        if isinstance(obj, bytes):
            return obj
        return obj.parser.build(obj)

    def _decode(self, data: bytes, context: cs.Context, path: cs.PathType) -> t.Any:
        compression = context.compression
        if isinstance(compression, cs.EnumIntegerString):
            compression = compression.intvalue

        if compression == CompressionMagic.DEEPMAP2 and len(data) >= 16:
            # DeepMap2 may contain lzfse compressed data
            return CARRenditionDeepMap2.parser.parse(data)
        return data

@dataclass_struct
class CARRenditionTheme:
    magic: bytes = csfield(cs.Const(b"MLEC"))  # CELM
    flags: int = csfield(cs.Int32ul)
    compression: CompressionMagic = tfield(
        CompressionMagic, cs.Enum(cs.Int32ul, CompressionMagic)
    )
    # Sometimes we have these sub-theme values
    theme_cbck: CARRenditionThemeCBCK = subcsfield(
        CARRenditionThemeCBCK, cs.Optional(CARRenditionThemeCBCK.struct)
    )
    length: int = csfield(cs.Int32ul)
    data: bytes | CARRenditionDeepMap2 = csfield(ThemeRenditionAdapter())


# internal
class it_renditions:
    def __init__(self, bom: BOM, key_format) -> None:
        self.bom = bom
        self.key_format = key_format

    def __iter__(self) -> t.Generator[tuple[dict, CARRenditionValue], t.Any, None]:
        tree = self.bom.tree_of(CAR_RENDITIONS_VARIABLE)
        for key, value in self.bom.iter_tree(tree):
            # The key stores  attributes
            values = cs.GreedyRange(cs.Int16ul).parse(key)
            attributes = dict(zip(self.key_format.identifiers, values))
            yield attributes, CARRenditionValue.parser.parse(value)
