#!/usr/bin/python3
"""
This module defines the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square, which is a special case of a rectangle
    where all sides have equal length.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The length of the square's sides.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string representation of the Square object.
        """
        return f"[Square] ({self.id}), {self.x}/{self.y} - {self.width}"
