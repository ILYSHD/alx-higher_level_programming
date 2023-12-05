#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """readfile a function that reads and print a file content

    arg: filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
