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

## Quickinfo
```yaml
obffpy quickinfo --file <path_to_obf_file>
```
### Output
```
Quicinfo about: <file_name>
.............
       Title: <title>
 Description: <description>
       Cover: <file_type> - <file_size>
       Pages: <num_pages>
```

## Unpack
```yaml
obffpy unpack [-h] --file <path_to_obf_file> -ef <export_folder_path>
```
### Output
```
Reading file...
Extracting and saveing cover...
Creating "pages" directory...
Extracting and saveing pages...
Generating book.json...
Done

<path_to_given_export_folder>
├── cover.jpeg
├── meta.json
└── pages (<page_count> File(s))

``` 


## Pack
```yaml
obffpy pack --saveFile <path_or_filename> --metaFile <book_meta_file>
```
Every path used in the metafile file, must be in the same folder as the metafile it self.
### Structure Example
```
MyBook
├── meta.json
├── cover.jpg
├── p1.jpg
└── some_folder
    └── p2.jpg
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
