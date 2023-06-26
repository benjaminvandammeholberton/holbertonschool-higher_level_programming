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
    def validator_size(self, value, name):
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

    def validator_position(self, value, name):
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
            raise TypeError(f"{name} must be an integer")
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")
        else:
            return value

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
        self.__width = self.validator_size(width, "width")
        self.__height = self.validator_size(height, "height")
        self.__x = self.validator_position(x, "x")
        self.__y = self.validator_position(y, "y")
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle."""
        self.__width = self.validator_size(width, "width")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle."""
        self.__height = self.validator_size(height, "height")

    @property
    def x(self):
        """Get the value of x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the value of x."""
        self.__x = self.validator_position(x, "x")

    @property
    def y(self):
        """Get the value of y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the value of y."""
        self.__y = self.validator_position(y, "y")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Display a visual representation of the rectangle using "#" characters.

        The height of the rectangle determines the number of rows, and
        the width determines the number of "#" characters in each row.
        The characters are
        printed to the console.

        If the rectangle has a positive y-coordinate, blank lines are printed
        before the rectangle to adjust the position.

        The x-coordinate of the rectangle determines the indentation of
        each row to adjust the position horizontally.
        """
        if self.__y > 0:
            print((self.__y - 1) * "\n")
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            for j in range(0, self.__width):
                print('#', end="")
            print("")

    def __str__(self):
        """
        Return a string representation of the Rectangle object.

        The string includes information about the rectangle's ID, position
        (x, y),
        width, and height. The format of the string is "[Rectangle] ID x/y -
        width/height".

        Returns:
            str: The string representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
        """
        Update the instance variables with the provided arguments.

        Args:
            *args: Variable number of arguments containing the values to update
            the instance variables.
        """
        variables = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, variables[i], arg)
