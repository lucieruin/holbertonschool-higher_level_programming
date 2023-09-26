#!/usr/bin/python3
def islower(c):
    char = ord(c)
    lower = False
    if char >= 97 and char <= 122:
        lower = True
    return lower
