#!/usr/bin/python3
"""
Function that adds 2 integers
args: a and b must be integers or float
Return: the addition of 2 integers
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers.
    """
    if type(a) is not int and type(a) is not float or a is None:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or b is None:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
