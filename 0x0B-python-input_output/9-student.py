#!/usr/bin/python3
"""student class"""


class Student:
    """body of the class"""

    def __init__(self, first_name, last_name, age):
        """initialize with first last and age"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        """dict represent tadtion for stud"""
        return self.__dict__
