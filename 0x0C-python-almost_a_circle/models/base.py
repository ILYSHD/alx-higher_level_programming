#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """Class that defines properties of Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ a function to initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
