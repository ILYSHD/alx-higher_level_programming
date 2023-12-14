#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines the rectangle properties"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ a function that initializes the rectangle instance

        Args: width, height, x, y, id
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if x != 0:
            if type(x) is not int:
                raise TypeError('x must be an integer')
            elif x <= 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = x
        if y != 0:
            if type(y) is not int:
                raise TypeError('y must be an integer')
            elif y <= 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = y

    def __str__(self):
        """a magic function to convert to string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        """a function that returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """a function that sets the value of width

        Args: value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a function that returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a function that sets the value of height

        Args: value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """a function that returns the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """a function that sets the value of x

        Args: value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """a function that returns the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """a function that sets the value of y

        Args: value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """function that return the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """a function that displays the rectangle"""
        print("\n"*self.__y, end='')
        for i in range(self.__height):
            print(" "*self.__x, end='')
            print("#"*self.__width, end='')
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """a method to return a dictionnary representation of the instance"""
        object_dic = {'id':self.id, 'width':self.__width, 'height':self.__height, 'x':self.__x,'y':self.__x}
        return object_dic
