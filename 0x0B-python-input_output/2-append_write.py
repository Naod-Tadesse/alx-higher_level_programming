#!/usr/bin/python3
"""append at the end"""


def append_write(filename="", text=""):
    """body of the function"""
    with open(filename, "a", encoding="utf-8") as openfile:
        return openfile.write(text)
