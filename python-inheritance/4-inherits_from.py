#!/usr/bin/python3
"""
This script defines a function that checks if an object is an instance of a
class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or
    indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited from
        the specified class,
              directly or indirectly. False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
