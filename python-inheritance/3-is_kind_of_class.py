#!/usr/bin/python3

""" returns True  otherwise False """


def is_kind_of_class(obj, a_class):
    """_summary_

    Args:
        obj (any): object to check
        a_class (any): given an object

    Return: True if object in instance otherwise false
    """

    return isinstance(obj, a_class)
