#!/usr/bin/python3
"""is_same_class module
"""


def is_same_class(obj, a_class):
    """is_same_class method

    Return: True if obj is instance of a_class
    """
    return type(obj) == a_class
