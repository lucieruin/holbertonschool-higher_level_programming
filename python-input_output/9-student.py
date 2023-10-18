#!/usr/bin/python3
""" Write a class Student """


class Student():
    """ class student """

    def __init__(self, first_name, last_name, age):
        """ Args:
                first_name(str): the first name
                last_name(str): the last name
                age(int): age
        """

        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
