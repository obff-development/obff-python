# Useage
- Class obff
    - [read](#read)
    - [write](#write)
    - [Class Book](https://github.com/obff-development/obff-python/tree/master/DOC/book.md)
    - [Class Cover](https://github.com/obff-development/obff-python/tree/master/DOC/cover.md)
    - [Class Page](https://github.com/obff-development/obff-python/tree/master/DOC/page.md)

## read
Type: `function`\
Syntax: `obff.read(<file_path>)`\
Args:\
&ensp;&ensp;&ensp;`file_path` __[str]__ Path to obf file to read.

Returns:\
&ensp;&ensp;&ensp;__[Book]__ Book Object of read obf file.

## write
Type: `function`\
Syntax: `obff.write(<file_path>, <book>, <?version>)`\
Args:\
&ensp;&ensp;&ensp;`file_path` __[str]__ Save path.
&ensp;&ensp;&ensp;`book` __[Book]__ [Book](https://github.com/obff-development/obff-python/tree/master/DOC/book.md) Object to save.
&ensp;&ensp;&ensp;`version` __[OBFF_VERSION]__ Fileformat version (*optional*)
