#!/usr/bin/python3
"""this function writes text to file"""


def write_file(filename="", text=""):
    """body"""
    with open(filename, "w", encoding="utf-8") as openfile:
        return openfile.write(text)
