
FILE_HEADERS = {
    "jpeg": [
        b'\xFF\xD8\xFF\xDB',
        b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01',
        b'\xFF\xD8\xFF\xEE',
        b'\xFF\xD8\xFF\xE1'
    ],
    "jp2": [
        b'\x00\x00\x00\x0C\x6A\x50\x20\x20\x0D\x0A\x87\x0A',
        b'\xFF\x4F\xFF\x51'
    ],
    "png": [
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    ],
    "bmp": [
        b'\x42\x4D'
    ],
    "pbm": [
        b'\x50\x31\x0A'
    ],
    "pgm": [
        b'\x50\x32\x0A'
    ],
    "ppm": [
        b'\x50\x33\x0A'
    ],
    "xpm": [
        b'\x2F\x2A\x20\x58\x50\x4D\x20\x2A\x2F'
    ],
    "jxl": [
        b'\x00\x00\x00\x0C\x4A\x58\x4C\x20\x0D\x0A\x87\x0A',
        b'\xFF\x0A'
    ]
}

def getFileExtension(file: bytes) -> str:
    decfile = file.decode("utf-8", "ignore")

    for key in FILE_HEADERS:
        headers = FILE_HEADERS[key]

        for header in headers:
            if decfile.startswith(header.decode("utf-8", "ignore")):
                return key

    return "bin"

def formatBytes(data: bytes, sep: str = " 0x") -> str:
    bytes_str = map("{:02x}".upper().format, data)
    return "0x" + sep.join(bytes_str)


def printErr(data: str):
    print("ERROR : {0}".format(data))

def format_bytes(size: int) -> str:
    power = 2**10 #(eq. to 1024)
    n = 0
    labels = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}

    while size > power:
        size = size / power
        n += 1

    return "{0}{1}B".format(str(round(size, 1)), labels[n])
