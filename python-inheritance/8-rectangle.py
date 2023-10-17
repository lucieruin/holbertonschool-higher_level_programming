#!/usr/bin/python3

""" a class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle """

    def __init__(self, width, height):
        """ Args:
                width: the width of the rectangle
                height: the height of the rectangle

        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
