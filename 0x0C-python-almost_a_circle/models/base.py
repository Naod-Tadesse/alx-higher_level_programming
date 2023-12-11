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

    @staticmethod
    def to_json_string(list_dictionaries):
        """dict to str"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
