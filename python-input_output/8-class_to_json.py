#!/usr/bin/python3
"""
This module provides a function for converting
a Python object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Convert a Python object to a JSON-serializable dictionary.

    Parameters:
        obj: The Python object to be converted.

    Returns:
        json_dict: A dictionary representing the
        JSON-serializable version of the object.
    """
    return vars(obj)
