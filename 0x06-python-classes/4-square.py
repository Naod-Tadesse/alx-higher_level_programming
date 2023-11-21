#!/usr/bin/python3
"""square blue print"""


class Square:
    """square class"""

    def __init__(self, size=0):

        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        if not (type(value) == int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        the area of the square
        Returns: int: area
        """
        return self.__size * self.__size
