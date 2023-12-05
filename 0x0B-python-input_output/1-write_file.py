#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write_file a function that writes a content to file

    arg: filename
    arg: text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        written_characters = f.tell()
    return written_characters
