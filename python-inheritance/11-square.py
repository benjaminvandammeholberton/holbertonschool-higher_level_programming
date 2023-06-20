#!/usr/bin/python3
"""
This script defines a class called 'BaseGeometry' with a method 'area' that
raises an exception.
"""

Rectangle = __import__('9-recangle').Rectangle


class Square(Rectangle):
    """
     A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def print(self):
        """
        Print the dimensions of the square.
        """
        print(f"[Square] {self.__size}/{self.__size}")

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            A string representation of the square in the format
            [Rectangle] size/size.
        """
        return (f"[Square] {self.__size}/{self.__size}")
