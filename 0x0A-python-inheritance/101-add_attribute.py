#!/usr/bin/python3
"""add attribute to obj"""


def add_attribute(dictio, attribute_name, value):
    """implementation"""

    if not hasattr(dictio, "__dict__") and not hasattr(type(dictio), "__slots__"):
        raise TypeError("Can't add new attribute")
    setattr(dictio, attribute_name, value)
