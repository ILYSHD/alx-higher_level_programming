#!/usr/bin/python3
"""append write module"""


def append_write(filename="", text=""):
    """append_file a function that appends a content to file

    arg: filename
    arg: text
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        written_characters = len(text)
    return written_characters
