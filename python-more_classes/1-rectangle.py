#!/usr/bin/python3
"""
Module that defines the Rectangle class
"""


class Rectangle:
    """
    Class that represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize an instance of Rectangle

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            value (int): The new width value
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value (int): The new height value
        """
        self.__height = value
