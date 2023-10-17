#!/usr/bin/python3

""" an empty class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ exception for area """

        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name, value):
        """ validates value
                Args:
                    name (str): the name of the value
                    value (int): the value

                Raises:
                    TypeError: if value is not an int
                    ValueError: if value less or equal to zero

        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
