#!/usr/bin/python3
"""the class square inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """blueprint to class square"""

    def __init__(self, size):
        """initialize size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, self.__size)
