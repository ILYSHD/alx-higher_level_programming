#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of square.

    Attributes:
        size: size of the square
    """
    def __init__(self, size=0):
        """creates a new instance of the square

        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
