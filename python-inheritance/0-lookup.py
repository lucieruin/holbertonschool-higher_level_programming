#!/usr/bin/python3

""" returns the list of available attributes and methods of an object """


def lookup(obj):
    """
    Args:
        obj: the object to return

    Return: the list of object
    """

    return (dir(obj))
