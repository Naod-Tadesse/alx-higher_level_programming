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
            raise TypeError("position must be a tubple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tubple of 2 positive integers")
        count = 0
        for i in value:
            if (type(i) == int) and i >= 0:
                count = count + 1
        if count != 2:
            raise TypeError("position must be a tubple of 2 positive integers")

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
