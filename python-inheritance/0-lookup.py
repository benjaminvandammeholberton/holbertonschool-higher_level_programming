#!/usr/bin/python3
"""
This script defines a function that returns a list of attributes and methods of
the specified object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the specified object.

    Args:
        obj: The object to inspect.

    Returns:
        A sorted list of strings representing the attributes and methods
        of the object.
    """
    return dir(obj)
