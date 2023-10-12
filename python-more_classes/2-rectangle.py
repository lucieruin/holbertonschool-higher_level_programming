#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """ class rectangle """

    def __init__(self, width=0, height=0):
        """ Args:
                width: rectangle width
                height: rectangle height

            Raises:
                TypeError: if width or height not integer
                ValueError: if width or height negative

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ def width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ def value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ def height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ def value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
