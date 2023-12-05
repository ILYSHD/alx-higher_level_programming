#!/usr/bin/python3
"""save to json module"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file writes an Object to a text file

    arg: my_obj
    arg: filename
    """
    with open(filename, 'w', encoding="utf-8") as a_file:
        a_file.write(json.dumps(my_obj))
