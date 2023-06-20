#!/usr/bin/python3
"""
This script defines a function that checks if an object is an instance of
a specified class or any of its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or any of
    its subclasses.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or
        any of its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
