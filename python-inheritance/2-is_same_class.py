#!/usr/bin/python3
"""
This script defines a function that checks if an object is exactly an
instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
        False otherwise.
    """
    return isinstance(obj, a_class)
