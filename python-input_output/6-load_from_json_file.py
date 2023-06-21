#!/usr/bin/python3
"""
This module provides a function for loading data from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return it.

    Parameters:
        filename (str): The name of the JSON file to load.

    Returns:
        data (dict or list): The loaded data from the JSON file.
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
