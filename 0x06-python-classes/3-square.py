#!/usr/bin/python3
"""definition of class called square"""


class Square:
    """
    basic definition that represents square
    """
    def __init__(self, size=0):
        """
            create new instance square
        """
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """
        return the result of squared size
        """
        return self.__size * self.__size
