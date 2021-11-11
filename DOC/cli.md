# OBFF > CLI

# Usage
```yaml
$ obffpy
usage: obffpy [-h] [-v] {quickinfo,unpack,pack} ...

OBFF CLI tool

positional arguments:
  {quickinfo,unpack,pack}
    quickinfo           Displays information of a OBF File in terminal
    unpack              Unpacks a OBF File
    pack                Packs data to a OBF File

optional arguments:
  -h, --help            show this help message and exit
  -v, --version

```

## Pack
```yaml
obffpy pack --file <export_filepath> --meta <book_meta_file>
```
### Book Meta File
```json
{
    "title": "Book Title",
    "description": "Book description",
    "cover": "cover.jpg",
    "pages": [
        "p1.jpg",
        "some_folder/p2.jpg"
    ]
}
```
### Structure
```
MyBook
├── meta.json
├── cover.jpg
├── p1.jpg
└── some_folder
    └── p2.jpg
```
