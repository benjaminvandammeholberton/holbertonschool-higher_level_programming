#!/usr/bin/python3
"""
This script defines a class called 'BaseGeometry' with a method 'area' that
raises an exception.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (float or int).
        """
        return self.__height * self.__width

    def print(self):
        """
        Print the dimensions of the rectangle.
        """
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            A string representation of the rectangle in the format
            [Rectangle] width/height.
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
