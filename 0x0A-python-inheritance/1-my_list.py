#!/usr/bin/python3
"""this class inherits from list class"""


class MyList(list):
    """this inherits from list"""

    def print_sorted(self):
        """this method returns sorted list"""
        print(sorted(self))
