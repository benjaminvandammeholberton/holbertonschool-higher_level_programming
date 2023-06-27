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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
