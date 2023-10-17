#!/usr/bin/python3

""" returns the list of available attributes and methods of an object """


def lookup(obj):
    """
    Args:
        obj: list object and method to return

    Return: the list of object and methods
    """
    return (dir(obj))
