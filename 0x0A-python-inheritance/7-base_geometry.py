#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry():
    """ Class that defines properties of a basegeometry."""
    def area(self):
        """a function that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
