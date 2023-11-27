#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """
    definition
    """
    def __init__(self, width=0, height=0):
        """
        initialization
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """rectangle width setter"""
        if not (type(value) == int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height of rectangle setter
        """
        if not (type(value) == int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        rectangle area get
        """
        return self.__width * self.__height

    def perimeter(self):
        """rectangle perimeter get"""
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        form of #
        """
        if self.__height == 0:
            return ""
        if self.__width == 0:
            return ""
        i = 0
        j = 0
        rectangle = ""
        while i < self.__height:
            j = 0
            while j < self.__width:
                rectangle = rectangle + "#"
                j += 1
            i += 1
            if (i == self.__height):
                pass
            else:
                rectangle = rectangle + "\n"
        return rectangle

    def __repr__(self):
        """represent in string"""
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        """print on delete"""
        print("Bye rectangle...")
