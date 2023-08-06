# libCAR
Python library to parse Catalog Asset Archives (CAR) of iOS Apps.

*this is a work in progress*

## Installation

Currently, this project does not have a PyPi installation candidate, so you have to clone the repository and run:
```bash
pip install .
```

## Basic Usage

> Info: All structures defined in python scripts are easy to understand as there are only field definitions (all classes are dataclasses).

### BOM (Build of Materials)

As Catalog Asset Archvies are special BOM (Build Of Materials) files, this project also provides a parser
for that file format. You can use the `BOM` class for almost all operations:

```python
import io
from libcar import BOM

# Either load all bytes and use an in-memory buffer or
# operate in a 'with' statement.
with open("Assets.car", "rb") as fp:
    data = fp.read()

# Create the BOM instance (loads some details automatically)
bom = BOM(io.BytesIO(data))

header = bom.header # get bom-header
variables = bom.variables # get all variables
indexes = bom.indexes # list all indexes (warning: commonly a huge list)

index = bom.index_of("VARIABLE_NAME") # Get index by name
tree = bom.get_tree(index) or bom.tree_of("VARIABLE_NAME")

# Iterate over all tree elements (key, value)
for key, value in bom.iter_tree(tree):
    # key and value will be raw bytes
    ...
```

### CAR (Catalog Asset Archive)

The creation of `CAR` objects may be handled easier compared to `BOM` objects as the class defines special parsing methods:

```python
from libcar import CAR

# PArse CAR directly from file stream
car = CAR.parse_file("Assets.car")

header = car.header # get CAR header information
meta = car.metadata # get CAR extended metadata information
key_format = car.key_format # get key format of renditions

for name, facet in car.facets:
    # name will be string and facet CARFacetValue
    ...

# list all appearance keys (if present)
appearance_keys = dict(car.appearance_keys)

# get and parse all stored renditions:
for attributes, rendition in car.iter_renditions(key_format):
    # NOTE: it is recommended to NOT use print(randition) here as the object
    # will store all of its raw data as a blob, which then would be printed
    ...
```


## CAR Scripts

### CAR-Extract

Use the script `car_extract.py` to extract all raw data structures (some images will be ignored). Note that themes and colors won't be extracted.

### CAR-Dump

The script `car_dump.py` offers a convienient way to inspect `*.car` files using the CLI. An example  of a dumped rendition:

```bash
python3 car_dump.py Assets.car -T RENDITIONS:4,5

> RENDITIONS:
    - Key: '<00000000 00000001 00000000 00009703 00000055 0000002A>'
        - magic: ISTC
        - version: 1
        - flags: 4
        - width: 0
        - height: 0
        - scale_factor: 0
        - pixel_format: PDF
        - color_space_id: 0
        - reserved_1: '\x00\x00\x00'
        - modification_date: 0
        - layout: <Layout.vector: 9>
        - reserved_2: 0
        - name: 'Arrow Clockwise.pdf'
        - info_len: 28
        - bitmap_count: 1
        - reserved_3: 0
        - payload_size: 3882
        - data:
            - headers:
                [0] => <class 'libcar.rendition.CARRenditionInfoHeader'>
                    - magic: <Magic.composition: 1004>
                    - length: 8
                    - content:
                        - blend_mode: 0
                        - opacity: 1.0
                [1] => <class 'libcar.rendition.CARRenditionInfoHeader'>
                    - magic: <Magic.bitmap_info: 1006>
                    - length: 4
                    - content:
                        - exif_orientation: 1
            - value:
                - magic: DWAR
                - compressed: 0
                - length: 3870
                - data: b"..."
```
