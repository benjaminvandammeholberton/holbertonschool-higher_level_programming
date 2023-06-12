#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, newsize):
        """
        Sets the size of the square.

        Args:
            newsize (int): The new size of the square.
        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(newsize, int):
            raise TypeError("size must be an integer")
        elif newsize < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = newsize
