#!/usr/bin/python3

""" an empty class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ exception for area """

        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
