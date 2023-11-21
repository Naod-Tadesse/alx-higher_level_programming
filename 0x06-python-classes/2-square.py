#!/usr/bin/python3
"""square class def"""


class Square:
    """
    blueprint for squre
    """
    def __init__(self, size=0):
        """
        create new instance of squre
        Args: size: size of the new square instance
        """
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
