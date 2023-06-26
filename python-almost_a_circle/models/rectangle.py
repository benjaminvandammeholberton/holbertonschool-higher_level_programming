#!/usr/bin/python3
"""
This module defines the Rectangle class
"""
from models.base import Base


def validator_size(value, name):
    """
    Validate the size value.

    Args:
        value (int): The value to be validated.
        name (str): The name of the attribute being validated.

    Returns:
        int: The validated value.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    elif value <= 0:
        raise ValueError(f"{name} must be > 0")
    else:
        return value


def validator_position(value, name):
    """
    Validate the position value.

    Args:
        value (int): The value to be validated.
        name (str): The name of the attribute being validated.

    Returns:
        int: The validated value.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name}, must be an integer")
    elif value < 0:
        raise ValueError(f"{name} must be >= 0")
    else:
        return value


class Rectangle(Base):
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
        id (int): The ID of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
            Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        self.__width = validator_size(width, "width")
        self.__height = validator_size(height, "height")
        self.__x = validator_position(x, "x")
        self.__y = validator_position(y, "y")
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle."""
        self.__width = self.__width = validator_size(width, "width")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle."""
        self.__height = self.__height = validator_size(height, "height")

    @property
    def x(self):
        """Get the value of x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the value of x."""
        self.__x = self.__x = validator_position(x, "x")

    @property
    def y(self):
        """Get the value of y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the value of y."""
        self.__y = validator_position(y, "y")
