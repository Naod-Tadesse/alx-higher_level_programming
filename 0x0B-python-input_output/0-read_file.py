#!/usr/bin/python3
"""function that reads file"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as openfile:
        print(openfile.read(), end="")
