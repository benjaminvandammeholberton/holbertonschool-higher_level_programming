#!/usr/bin/python3
"""
function that prints a square with the character #.
Args: size is the size length of the square
Return: print a square
"""


def print_square(size):
    """
    function that prints a square with the character #.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(0, size):
        print("#" * size)
