#!/usr/bin/python3
""" write a string """


def write_file(filename="", text=""):
    """ write a string """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
