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

    def integer_validator(self, name, value):
        """

        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
