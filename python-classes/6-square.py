#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__validate_size(size)
        self.__validate_position(position)

    def __validate_size(self, size):
        """
        Validates the size of the square.

        Args:
            size (int): The size to validate.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
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
        """
        self.__validate_size(newsize)

    def my_print(self):
        """
        Prints a visual representation of the Square instance using
        '#' characters.

        If the size of the square is 0, it prints an empty line.
        Each row of the square is represented by '#'
        characters printed horizontally.
        The number of rows and columns is equal to the size of the square.
        The position of the square is taken into account by adding leading
        spaces.
        """
        if self.size == 0:
            print()
        for k in range(self.position[1]):
            print()
        for i in range(self.size):
            for m in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

    def __validate_position(self, value):
        """
        Validates the position of the square.

        Args:
            value (tuple): The position to validate.
        Raises:
            TypeError: If the position is not a tuple of 2 integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 positive\
                                integers")
        else:
            self.__position = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        """
        Sets the position of the square.

        Args:
            new_position (tuple): The new position of the square.
        """
        self.__validate_position(new_position)
