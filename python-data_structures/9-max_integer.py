#!/usr/bin/python3
def max_integer(my_list=[]):
    maxNum = my_list[0] if my_list else None
    for index in my_list:
        if index > maxNum:
            maxNum = index
    return maxNum
