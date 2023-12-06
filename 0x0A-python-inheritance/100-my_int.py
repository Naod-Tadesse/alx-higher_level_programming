#!/usr/bin/python3
"""blue print class myint"""


class MyInt(int):
    """implementation"""

    def __ne__(self, number):
        """not equal implementation"""
        return not super().__ne__(number)

    def __eq__(self, number):
        """equal implementation"""
        return not super().__eq__(number)
