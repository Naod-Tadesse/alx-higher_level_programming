#!/usr/bin/python3
"""after appdnd"""


def append_after(filename="", search_string="", new_string=""):
    """body"""

    string = ""
    with open(filename, 'r') as openfile:
        reads = openfile.readlines()
        for everyline in reads:
            string += everyline
            if search_string in everyline:
                string += new_string

    with open(filename, 'w') as openedfile:
        openedfile.write(string)
