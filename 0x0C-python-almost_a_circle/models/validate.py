#!/usr/bin/python3

def validate(unit, value):
    """validator"""

    if not (isinstance(unit, int)):
        raise TypeError(f"{unit} must be an integer")
    if (unit == "x"):
        if value < 0:
            raise ValueError(f"{unit} must be >= 0")
    if (unit == "y"):
        if value < 0:
            raise ValueError(f"{unit} must be >= 0")
    if value <= 0:
        raise ValueError(f"{unit} must be > 0")
