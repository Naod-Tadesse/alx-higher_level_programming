#!/usr/bin/python3
"""
load json
"""
import json


def load_from_json_file(filename):
    """from json file to obj"""
    with open(filename) as openfile:
        return json.load(openfile)
