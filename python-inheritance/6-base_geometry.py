#!/usr/bin/python3

""" an empty class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ exception for area """

        raise Exception(f"{self.area.__name__}() is not implemented")
