#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    for key in new_list:
        new_list[key] = new_list[key] * 2
    return new_list
