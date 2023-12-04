#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines properties of a Rectagle."""
    def __init__(self, width, height):
        """Initialize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

