#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of square by: (based on 4-square.py).

    Attributes:
        width: width of the rectangle.
        height: height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creates a new instance of the rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __del__(self):
        """destructor
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    def __str__(self):
        """a magic function to convert to string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    result = result + str(self.print_symbol)
                if i != self.__height - 1:
                    result = result + "\n"
            return result

    def __repr__(self):
        """a fucntion that return the representation of rectangle
        """
        return f'{type(self).__name__}({self.__width}, {self.__height})'

    @property
    def width(self):
        """Returns the width of a square
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width.

        Args:
            value (int): width of a square.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of a square
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height.

        Args:
            value (int): height of a square.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """return the rectangle permiter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
