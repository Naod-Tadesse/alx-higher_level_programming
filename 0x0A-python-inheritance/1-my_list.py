#!usr/bin/python3
"""this class inherits from list class"""


class MyList(list):
    """this inherits from list"""

    def __init__(self):
        """instantiate"""
        super().__init__()

    def print_sorted(self):
        """this method returns sorted list"""
        print(sorted(self))
