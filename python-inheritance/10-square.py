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
        Validates that the value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            A string representation of the rectangle in the format
            [Rectangle] width/height.
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")


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
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
