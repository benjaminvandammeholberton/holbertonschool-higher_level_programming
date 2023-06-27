#!/usr/bin/python3
"""
This module defines the Base class
"""
import json


class Base:
    """
    This is the Base class.
    It serves as the base class for other classes in the module.
    """
    __nb_objects = 0
    list_dictionaries = []

    def __init__(self, id=None):
        """
        This is the constructor for the Base class.
        It initializes the object and increments the __nb_objects counter.

        Args:
            id (int, optional): An ID value for the object. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
        self.list_dictionaries.append(self.to_dictionary())

    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON-formatted string representation of the list of
            dictionaries.
                If the input list is None or empty, returns "[]".
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
