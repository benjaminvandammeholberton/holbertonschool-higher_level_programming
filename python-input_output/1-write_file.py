#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file.

    Args:
        filename (str): The name of the file to write to. If not provided,
        an empty string is used.
        text (str): The text to be written to the file.

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
