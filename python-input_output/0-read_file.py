#!/usr/bin/python3
""" read a file """


def read_file(filename=""):
    """ read file
        Arg: filename: the file to read
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
