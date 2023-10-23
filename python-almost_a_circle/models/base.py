#!/usr/bin/python3
""" first class Base """


class Base():
    """ class base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init base """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integerValid(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def integerValid2(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
