#!/usr/bin/python3
"""
This module defines a function that prints the contents of a file
"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): The name of the file to be read. If not provided, an
        empty string is used.

    Returns:
        None
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
