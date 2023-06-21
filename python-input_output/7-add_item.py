#!/usr/bin/python3
"""
This script adds command-line arguments to a Python list and saves
it to a JSON file.
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data.append(sys.argv[1:])

save_to_json_file(data, filename)
