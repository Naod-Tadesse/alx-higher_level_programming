#!/usr/bin/python3
"""the blueprint class for classes"""
import json


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
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """file to save"""
        file_name = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []
        list_objs = [item.to_dictionary() for item in list_objs]
        with open(file_name, 'w') as opened:
            opened.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """load"""
        if json_string is None:
            return []
        return json.loads(json_string)
