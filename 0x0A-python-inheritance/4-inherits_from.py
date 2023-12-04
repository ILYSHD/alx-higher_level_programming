#!/usr/bin/python3
"""inherits_from module
"""


def inherits_from(obj, a_class):
    """inherits_from method

    Return: True if obj is an instance of an inherited class of a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
