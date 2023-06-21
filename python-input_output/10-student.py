#!/usr/bin/python3
"""
This module defines a Student class and provides
methods for working with student objects.
"""


class Student:
    """
    Represents a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    my_dict[element] = self.__dict__[element]
            return my_dict
