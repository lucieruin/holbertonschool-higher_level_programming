#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if my_list is None:
        my_list = []
    for integer in my_list:
        print("{:d}".format(integer))
