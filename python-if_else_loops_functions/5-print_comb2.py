#!/usr/bin/python3
separator = ", "
for num in range(0, 100):
    if num == 99:
        separator = "\n"
    print("{:02d}".format(num), end=separator)
