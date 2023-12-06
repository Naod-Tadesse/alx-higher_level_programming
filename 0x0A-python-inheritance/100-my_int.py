#!/usr/bin/python3
"""blue print class myint"""


class MyInt:
    """implementation"""

    def __ne__(self, number):
        """not equal implementation"""
        return not super().__ne__(number)

    def __eq__(self, other):
        """equal implementation"""
        return not super().__eq__(number)
