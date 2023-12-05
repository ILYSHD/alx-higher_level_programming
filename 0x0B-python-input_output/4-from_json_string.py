#!/usr/bin/python3
"""from json string module"""
import json


def from_json_string(my_str):
    """from_json_string returns an object

    arg: my_str
    """
    return json.loads(my_str)
