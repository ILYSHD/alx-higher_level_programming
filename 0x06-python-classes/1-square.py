#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of square.

    Attributes:
        size: size of the square
    """
    def __init__(self, size):
        """creates a new instance of the square

        Args:
            size: size of the square
        """
        self.__size = size
