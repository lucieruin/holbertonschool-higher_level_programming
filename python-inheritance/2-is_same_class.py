#!/usr/bin/python3

""" returns True if the object is exactly an instance """


def is_same_class(obj, a_class):
    """check if instance of class

    Args:
        obj (any): object to check
        a_class (any): given object

    Return:
        booleen: true if type is instance or false if not
    """

    return type(obj) is a_class
