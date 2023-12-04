#!/usr/bin/python3
"""function returns true if obj is instance or inherits"""


def is_kind_of_class(obj, a_class):
    """the functions implementation """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
