#!/usr/bin/python3
"""
This module contains utility functions for working with JSON.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON formatted string to a Python object.

    Args:
        my_str (str): The JSON formatted string to be converted.

    Returns:
        Any: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
