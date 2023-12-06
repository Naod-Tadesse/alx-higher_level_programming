#!/usr/bin/python3
"""add attribute to obj"""


def add_attribute(di, diname, divalue):
    """implementation"""

    if hasattr(di, "__dict__"):
        setattr(di, diname, divalue)
    else:
        raise TypeError("can't add new attribute")
