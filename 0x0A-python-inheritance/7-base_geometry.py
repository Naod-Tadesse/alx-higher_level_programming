#!/usr/bin/python3
"""the base geometry"""


class BaseGeometry:
    """implementation"""

    def area(self):
        """no area implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """an integer validator"""
        if (type(value) != int):
            raise TypeError("name must be an integer")
        if (value <= 0):
            raise ValueError("name must be greater than 0")
