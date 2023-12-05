#!/usr/bin/python3
"""Student class module"""


class Student():
    """ Class that defines properties of a Student."""
    def __init__(self, first_name, last_name, age):
        """a method to initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a method that retrieves a dictionary representation"""
        if not isinstance(attrs, list):
            return self.__dict__
        for elt in attrs:
            if not isinstance(elt, str):
                return self.__dict__
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
