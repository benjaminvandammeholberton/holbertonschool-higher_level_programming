#!/usr/bin/python3
"""
This module defines the Base class
"""


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
