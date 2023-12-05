#!/usr/bin/python3
"""append json representation to file"""
import json


def save_to_json_file(my_obj, filename):
    """implementation"""
    with open(filename, "w", encoding="utf-8") as openfile:
        return json.dump(my_obj, openfile)
