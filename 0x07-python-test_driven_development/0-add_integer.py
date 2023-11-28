#!/usr/bin/python3
"""function for adding two ints"""

def add_integer(a, b=98):
    """add two ints"""
    if not ((type(a) == int) or (type(a) == float)):
        raise TypeError("a must be an integer")
    if not ((type(b) == float) or (type(b) == int)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
