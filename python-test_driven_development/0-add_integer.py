#!/usr/bin/python3

""" add 2 integers """


def add_integer(a, b=98):
    """ args:
            a(int): number
            b(int): number set defauts to 98

        raises:
            TypeError: if  or b is not an int or a float

        Return: result(a+b)
    """

    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
