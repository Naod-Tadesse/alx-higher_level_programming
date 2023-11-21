#!/usr/bin/python3
"""class blueprint for square"""


class Square:
    """structure for square"""

    def __init__(self, size=0, position=(0, 0)):
        """object square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size get"""
        return self.__size

    @size.setter
    def size(self, value):
        if not (type(value) == int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (type(value) == tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print using #"""
        i = 0
        j = 0
        k = 0
        if self.__size == 0:
            print("")
        while k < self.position[1]:
            print()
            k = k + 1
        while i < self.__size:
            j = 0
            while j < self.__position[0]:
                print(" ", end="")
                j = j + 1
            j = 0
            while j < self.__size:
                print("#", end="")
                j = j + 1
            i = i + 1
            print("")
