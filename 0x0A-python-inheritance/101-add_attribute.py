#!/usr/bin/python3
"""add attribute to obj"""


def add_attribute(dictio, name, value):
    """implementation"""

    if not hasattr(dictio, "__dict__"):
        raise TypeError("Can't add new attribute")
    setattr(dictio, name, value)
