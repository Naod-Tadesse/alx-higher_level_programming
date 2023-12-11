#!/usr/bin/python3
"""the blueprint class for classes"""


class Base:
    """base class for all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize vaiable"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
