#!/usr/bin/python3
"""blueprint for object square"""


class Square:
    """square blueprint"""

    def __init__(self, size=0):
        """
        square object initialize
        """
        if not (type(size) == int):
            raise TypeError("size must be and integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not (type(value) == int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print using #"""
        i = 0
        j = 0
        if self.__size == 0:
            print("")
        while i < self.__size:
            j = 0
            while j < self.__size:
                print("#", end="")
                j = j + 1
            i = i + 1
            print("")
