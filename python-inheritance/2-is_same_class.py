#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class,
        False otherwise.
    """
    return isinstance(obj, a_class)
