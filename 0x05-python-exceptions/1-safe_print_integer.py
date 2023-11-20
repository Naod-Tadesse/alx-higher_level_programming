#!/usr/bin/python3
def safe_print_integer(value):
    """this function prints integer"""
    try:
        print("{:d}".format(value), end="")
        print()
        return True
    except:
        return False
