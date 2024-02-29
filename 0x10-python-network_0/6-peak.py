#!/usr/bin/python3
"""the highest of the neighbours"""


def find_peak(list_of_integers):
    """this calculates the peak"""
    if list_of_integers:
        lef = 0
        r = len(list_of_integers) - 1

        while lef < r:
            m = (lef + r) // 2
            lef, r = (m + 1, r) \
                if list_of_integers[m] < list_of_integers[m + 1] else (lef, m)
        return list_of_integers[lef]
    else:
        return None
