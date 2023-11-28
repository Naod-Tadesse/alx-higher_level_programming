#!/usr/bin/python3
def magic_string():
    magic_string.number = getattr(magic_string, 'number', -1) + 1
    return ', '.join(['BestSchool'] * (magic_string.number + 1))
