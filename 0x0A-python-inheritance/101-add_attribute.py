#!/usr/bin/python3
"""add attribute to obj"""


def add_attribute(dictio, attribute_name, value):
    """implementation"""

    if hasattr(dictio, "__dict__"):
        setattr(dictio, attribute_name, value)
    else:
        raise TypeError("can't add new attribute")
