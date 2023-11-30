#!/usr/bin/python3
"""square printer"""


def print_square(size):
    """prints square with # character"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j = j + 1
        i = i + 1
        print()
