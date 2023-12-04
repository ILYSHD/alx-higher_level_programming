#!/usr/bin/python3
"""Square class module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class that defines properties of a Square."""
    def __init__(self, size):
        """Initialize Square method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """defines the area method"""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
