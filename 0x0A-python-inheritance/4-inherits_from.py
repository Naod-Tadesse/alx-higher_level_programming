#!/usr/bin/python3
"""this function return true if obj is from class that is from another class"""


def inherits_from(obj, a_class):
    """implementation"""

    if (type(obj) != a_class and issubclass(type(obj), a_class)):
        return True
    else:
        return False
