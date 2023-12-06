#!/usr/bin/python3
"""
rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherit"""

    def __init__(self, width, height):
        """init"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """computes area"""
        return (self.__width) * (self.__height)

    def __str__(self):
        """return the string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
