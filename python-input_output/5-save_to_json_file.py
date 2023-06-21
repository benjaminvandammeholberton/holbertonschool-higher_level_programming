#!/usr/bin/python3
"""
This module contains utility functions for working with JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes a Python object to JSON and saves it to a file.

    Args:
        my_obj (Any): The Python object to be serialized to JSON.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
