#!/usr/bin/python3
class Rectangle:
    """rectangle object"""
    def __init__(self, width=0, height=0):
        """object initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """to receive the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """a method to set width"""
        if not (type(value) == int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """object's height setter"""
        if not (type(value) == int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """this method computes the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """this method computes the perimeter of a rectangle"""
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
