import os
import json
from argparse import ArgumentParser
import obff
from obff.cli.utils import format_bytes, printErr, getFileExtension
from obff.cli.terminal import Loader


parser = ArgumentParser(description="OBFF CLI tool")
parser.add_argument("-v", "--version", action="store_true")
subparsers = parser.add_subparsers()

sp_cmd_quicinfo = subparsers.add_parser('quickinfo', help='Displays information of a OBF File in terminal')
sp_cmd_quicinfo.set_defaults(cmd = 'quickinfo')
sp_cmd_quicinfo.add_argument("--file", type=str, required=True, help="OBF File to display info form")

sp_cmd_unpack = subparsers.add_parser('unpack', help='Unpacks a OBF File')
sp_cmd_unpack.set_defaults(cmd = 'unpack')
sp_cmd_unpack.add_argument("--file", type=str, required=True, help="OBF File to extract from")
sp_cmd_unpack.add_argument("-sd", "--saveDir", type=str, required=True, help="Directory where pages will be saved to")

sp_cmd_pack = subparsers.add_parser('pack', help='Packs data to a OBF File')
sp_cmd_pack.set_defaults(cmd = 'pack')
sp_cmd_pack.add_argument("-t", "--title", type=str, required=True, help="Description for book")
sp_cmd_pack.add_argument("-d", "--description", type=str, required=True, help="Description for book")
sp_cmd_pack.add_argument("--file", type=str, required=True, help="Export path/file")
sp_cmd_pack.add_argument("-c", "--cover", type=str, required=True, help="Path to cover image")
sp_cmd_pack.add_argument("-p", "--pages", type=str, required=True, help="Directory containing pages files (labled 1, 2 etc.)")


args = parser.parse_args()

# Quickinformation about a OBF File
def quicky(path: str):
    fname = os.path.basename(path)
    mbook = obff.read(path)

    cover_size = len(mbook._cover_bytes)
    formatted_desc = mbook.description.splitlines()

    lines = [
        "Quicinfo about: {0}".format(fname),
        ".............",
        "       Title: {0}".format(mbook.title),
        " Description: {0}".format("\n".ljust(15, " ").join(formatted_desc)),
        "       Cover: {0} - {1}".format(getFileExtension(mbook._cover_bytes), format_bytes(cover_size)),
        "       Pages: {0}".format(mbook.page_count),
    ]

    print("\n".join(lines))

# Unpack OBF File
def unpack(src_path: str, exp_path: str):
    if not os.path.exists(exp_path) or not os.path.isdir(exp_path):
        return

    fn_cover = "cover."
    dir_pages = os.path.join(exp_path, "pages")
    fn_pages = []

    print("Reading file...")
    mbook = obff.read(src_path)

    # Write: Cover to file
    fn_cover += getFileExtension(mbook._cover_bytes)
    print("Extracting and saveing cover...")
    f_cover = open(os.path.join(exp_path, fn_cover), "wb")
    f_cover.write(mbook._cover_bytes)
    f_cover.close()

    if not os.path.exists(dir_pages) or not os.path.isdir(dir_pages):
        print("Creating \"pages\" directory...")
        os.mkdir(dir_pages)

    # Write: Pages to file
    print("Extracting and saveing pages...")
    pages = mbook.pages
    num_pages = len(pages)
    lder = Loader("Page 1 of {0}".format(str(num_pages)), "").start()
    for i in range(num_pages):
        lder.update_desc("Page {0} of {1}".format(str(i), str(num_pages)))

        page = pages[i]
        fname = "page_{0}.{1}".format(page.number, getFileExtension(page.content))
        fn_pages.append("pages/" + fname)
        file = open(os.path.join(dir_pages, fname), "wb")
        file.write(page.content)
        file.close()

    lder.stop()

    print("Generating book.json...")
    # Creating book.json (contains all informations such a the title)
    content = {
        "title": mbook.title,
        "description": mbook.description,
        "cover": fn_cover,
        "pages": fn_pages
    }

    book_meta = open(os.path.join(exp_path, "book.json"), "w")
    book_meta.write(json.dumps(content))
    book_meta.close()

    print("Done\n")

    # Print pretty dir tree
    pages_fc = os.listdir(dir_pages)
    lines_ = [
        exp_path,
        "├── {0}".format(fn_cover),
        "├── book.json",
        "└── pages ({0} File(s))".format(len(pages_fc))
    ]

    print("\n".join(lines_))



def start():
    if args.version:
        print("OBFF CLI Tool v{0} [OBFF Parser v{1}]".format(obff.cli.version, obff.version))
        return

    if not "cmd" in args:
        parser.print_help()
        return

    if args.cmd == "quickinfo":
        quicky(os.path.join(os.getcwd(), args.file))


    elif args.cmd == "unpack":
        path_src_file = os.path.join(os.getcwd(), args.file)
        path_exp_dir = os.path.join(os.getcwd(), args.saveDir)

        unpack(path_src_file, path_exp_dir)

    elif args.cmd == "pack":
        pass
