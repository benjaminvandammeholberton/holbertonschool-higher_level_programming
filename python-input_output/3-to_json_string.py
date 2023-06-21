#!/usr/bin/python3
"""
This module contains utility functions for working with JSON.
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON formatted string.

    Args:
        my_obj (Any): The Python object to be converted to JSON.

    Returns:
        str: The JSON formatted string representation of the object.
    """
    return json.dumps(my_obj)
