#!/usr/bin/python3
"""module 4
"""


class Square:
    """Access and update private attribute"""
    def __init__(self, size=0):
        """init square"""
        self.size = size

    @property
    def size(self):

        """def size square"""
        return (self.__size)

    @size.setter
    def size(self, value):

        """def value and raise exceptions"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """return the current square"""
        return (self.__size ** 2)

    def my_print(self):

        """print a square"""
        if self.__size == 0:
            print()
        else:
            for index in range(self.size):
                print("#".format(self.__size) * self.__size)
