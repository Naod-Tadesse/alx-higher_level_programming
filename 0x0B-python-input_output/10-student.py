#!/usr/bin/python3
"""blueprint class student"""


class Student:
    """Student class to represent student information"""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name, last name, and age"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            dictiona = {a: getattr(self, a) for a in attrs if hasattr(self, a)}
            return dictiona
        return self.__dict__
