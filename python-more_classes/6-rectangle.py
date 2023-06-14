#!/usr/bin/python3
"""
Module that defines the Rectangle class
"""


class Rectangle:
    """
    Class that represents a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize an instance of Rectangle

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
            number_of_instances (int): Keeps track of the
            number of Rectangle instances created.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle, with '#'
            characters forming the shape.
        """
        if self.width == 0 or self.height == 0:
            return ""

        row = "#" * self.width
        result = [row] * self.height
        return "\n".join(result)

    def __repr__(self):
        """
        Return a string representation of the rectangle that can
        be used to recreate the object.

        Returns:
            str: A string representing the rectangle in the
            format "Rectangle(width, height)".

        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        Perform any necessary cleanup operations before the
        object is destroyed.

        This method is automatically called when the object
        is about to be garbage collected.

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
