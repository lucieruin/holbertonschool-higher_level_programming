#!/usr/bin/python3

""" returns True if the object is exactly an instance of the specified class ; otherwise False """


def is_same_class(obj, a_class):
    """check if instance of class

    Args:
        obj (any): object to check
        a_class (any): given object

    Return:
        booleen: true if type is instance or false if not
    """

    return type(obj) == a_class
