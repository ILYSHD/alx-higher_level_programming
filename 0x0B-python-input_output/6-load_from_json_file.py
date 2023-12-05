#!/usr/bin/python3
"""load from json file module
"""

import json


def load_from_json_file(filename):
    """load json file

    args: filename
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
