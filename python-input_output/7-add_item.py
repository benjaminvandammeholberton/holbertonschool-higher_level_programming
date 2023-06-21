#!/usr/bin/python3
"""
This script adds command-line arguments to a Python list and saves
it to a JSON file.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Main function that adds command-line arguments to a Python
    list and saves it to a JSON file.

    Arguments:
    - None

    Returns:
    - None

    Side Effects:
    - Appends command-line arguments to the data list.
    - Saves the updated list to the JSON file.

    Example:
    >>> main()
    ["Best", "School"]
    """


filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data.append(sys.argv[1:])

save_to_json_file(data, filename)
