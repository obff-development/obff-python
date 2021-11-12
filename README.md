## obff [python] [![Downloads](https://pepy.tech/badge/obff)](https://pypi.org/project/obff) [![](https://img.shields.io/pypi/v/obff)](https://pypi.org/project/obff/)
Open Book File Format Handler for python
See [specs](https://github.com/obff-development/obff-spec/blob/main/README.md) for more informations.

## Example
### structure
```
example_book
├── example.py
├── hello_world.obff
├── book_content
│   ├── cover.png
│   ├── page_1.png
│   ├── page_2.png
│   └── page_3.png
└── exported_book
```
### Snippet Write
```python
import obff
import os # NOT REQUIRED TO IMPORT

myBook = obff.Book()
myBook.title = "Hello World Book"
myBook.description = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
myBook.cover = obff.Cover(open("./book_content/cover.png", "rb").read())

pages = natsorted(os.listdir("./book_content"))
for page in pages:
    if page.startswith("cover"):
        continue

    path = os.path.join("./book_content", page)
    myBook.addPage(obff.Page(open(path, "rb").read()))

obff.write("./hello_world.obff", myBook)
```

### Snippet Read
```python
import obff

myBook = obff.read("./hello_world.obff")
print("Title: {0}".format(myBook.title))
print("Description: {0}".format(myBook.description))
myBook.cover.saveImage("./exported_book/cover.jpg")
```
