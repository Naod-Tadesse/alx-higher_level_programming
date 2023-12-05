#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """implement"""
    if n <= 0:
        return []

    slus = [[1]]
    while len(slus) != n:
        i = 0
        giziawi = [1]
        slus1 = slus[-1]
        while i < len(slus1):
            if i + 1 < len(slus1):
                giziawi.append(slus1[i] + slus1[i + 1])
            i = i + 1
        giziawi.append(1)
        slus.append(giziawi)
    return slus
