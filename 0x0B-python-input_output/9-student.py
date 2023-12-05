#!/usr/bin/python3
"""Student class module"""


class Student():
    """ Class that defines properties of a Student."""
    def __init__(self, first_name, last_name, age):
        """a method to initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a method that retrieves a dictionary representation"""
        return self.__dict__
