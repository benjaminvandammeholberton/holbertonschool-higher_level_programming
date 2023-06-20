#!/usr/bin/python3
"""
This script defines a class called 'BaseGeometry' with a method 'area' that
raises an exception.
"""


class BaseGeometry:
    """
    This class serves as a base for defining geometric classes.
    """
    def area(self):
        """
        Raises an exception indicating that the 'area' method is not
        implemented.
        """
        raise Exception("area() is not implemented")
