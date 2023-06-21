#!/usr/bin/python3
"""
This module contains a function for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends the specified text to a file.

    Args:
        filename (str): The name of the file to append to. If not provided,
        an empty string is used.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
