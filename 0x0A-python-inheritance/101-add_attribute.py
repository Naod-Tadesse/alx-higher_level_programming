#!/usr/bin/python3
"""add attribute to obj"""


def add_attribute(dictio, name, value):
    """implementation"""

    if hasattr(dictio, "__dict__"):
        setattr(dictio, name, value)
    else:
        raise TypeError("Can't add new attribute")
