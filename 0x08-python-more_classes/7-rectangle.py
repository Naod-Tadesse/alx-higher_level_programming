#!/usr/bin/python3
"""rectangle class definition"""


class Rectangle:
    """
    class def
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        create
        object
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """the width of the rec set"""
        if not (type(value) == int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height of the rec get"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height set
        """
        if not (type(value) == int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area compute
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
        #
        form
        """
        if self.__height == 0:
            return ""
        if self.__width == 0:
            return ""
        i = 0
        j = 0
        rectangle = ""
        if (type(Rectangle.print_symbol) == list):
            symbol = ''.join(str(item) for item in self.print_symbol)
        else:
            symbol = str(self.print_symbol)
        while i < self.__height:
            j = 0
            while j < self.__width:
                rectangle = rectangle + Rectangle.print_symbol
                j += 1
            i += 1
            if (i == self.__height):
                pass
            else:
                rectangle = rectangle + "\n"
        return '\n'.join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """string representation"""
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        """delete task"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
