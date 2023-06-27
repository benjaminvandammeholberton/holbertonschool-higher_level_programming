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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = self.validator_size(value, "width")
        self.height = self.validator_size(value, "height")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square.

            Args:
                *args: Variable number of positional arguments.
                    - If provided, the arguments are treated in the following
                    order:
                        - arg1 (int): The new value for the id attribute.
                        - arg2 (int): The new value for the size attribute.
                        - arg3 (int): The new value for the x attribute.
                        - arg4 (int): The new value for the y attribute.
                **kwargs: Variable number of keyword arguments.
                    - If provided, the arguments are treated as attribute-value
                    pairs,
                    where the attribute is the name of the attribute to update,
                    and the value is the new value to assign.

            Note:
                - If both positional arguments (*args) and keyword arguments
                (**kwargs) are provided,
                the positional arguments will take precedence, and the keyword
                arguments will be ignored.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square instance.

        Returns:
        dict: A dictionary containing the instance's attributes and their
        values.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
