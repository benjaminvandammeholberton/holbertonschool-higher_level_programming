#!/usr/bin/python3
"""
This module defines the Rectangle class
"""
from models.base import Base


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self, new_width):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, new_width):
        """Set the width of the rectangle."""
        self.__width = new_width

    @property
    def height(self, new_height):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, new_height):
        """Set the height of the rectangle."""
        self.__height = new_height

    @property
    def x(self, new_x):
        """Get the value of x."""
        return self.__x

    @x.setter
    def x(self, new_x):
        """Set the value of x."""
        self.__x = new_x

    @property
    def y(self, new_y):
        """Get the value of y."""
        return self.y

    @y.setter
    def y(self, new_y):
        """Set the value of y."""
        self.__y = new_y
