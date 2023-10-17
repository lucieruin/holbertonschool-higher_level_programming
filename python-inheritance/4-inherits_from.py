#!/usr/bin/python3

""" returns True  otherwise False """


def inherits_from(obj, a_class):
    """returns True otherwise false

    Args:
        obj (any): object to check
        a_class (any): given an object

    Return: True if object in instance otherwise false
    """

    return isinstance(obj, a_class) and  not issubclass(a_class, obj.__class__)
