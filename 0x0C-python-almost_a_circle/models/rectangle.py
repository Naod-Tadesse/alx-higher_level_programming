#!/usr/bin/python3
"""a class rectangle that inherits from base class"""
from models.base import Base
from models.validate import validate


class Rectangle(Base):
    """class body"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class initialization"""
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        validate(value, "height")
        self.__height = value

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        validate(value, "width")
        self.__width = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        validate(value, "x")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        validate(value, "y")
        self.__y = value

    def area(self):
        """computes area"""
        return (self.__height * self.__width)

    def display(self):
        """displaty rect usint #"""
        for i in range(self.height):
            for k in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """srt rep"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} -"
                f" {self.width}/{self.height}")
