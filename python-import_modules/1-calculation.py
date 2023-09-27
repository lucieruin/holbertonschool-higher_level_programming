#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    sum = add(a, b)
    result = sub(a, b)
    multi = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, result))
    print("{} * {} = {}".format(a, b, multi))
    print("{} / {} = {}".format(a, b, divi))
