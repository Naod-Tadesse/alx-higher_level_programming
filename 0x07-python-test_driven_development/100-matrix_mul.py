#!/usr/bin/python3
"""multiplication of matrices"""


def matrix_mul(m_a, m_b):
    if not (type(m_a) == list):
        raise TypeError("m_a must be a list")
    if not (type(m_b) == list):
        raise TypeError("m_b must be a list")
    for item in m_a:
        if not (type(m_a) == list):
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if not (type(m_b) == list):
            raise TypeError("m_b must be a list of lists")
    if (m_a == [] or m_a == [[]]):
        raise TypeError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise TypeError("m_b can't be empty")


    for item in m_a:
        for element in item:
            if not (type(element) == int or type(element) == float):
                raise TypeError("m_a should contain only integers or floats")

    for item in m_b:
        for element in item:
            if not (type(element) == int or type(element) == float):
                raise TypeError("m_b should contain only integers or floats")

    for item in m_a:
        if not (len(item) == len(m_a[0])):
            raise TypeError("each row of m_a must should be of the same size")

    for item in m_b:
        if not (len(item) == len(m_b[0])):
            raise TypeError("each row of m_b must should be of the same size")
    multiplied = []
    a = 0
    b = 0
    c = 0
    while a < len(m_a):
        mat = []
        b = 0
        while b < len(m_b[0]):
            accumulator = 0
            c = 0
            while c < len(m_b):
                accumulator = accumulator + (m_a[a][c] * m_b[c][b])
                c = c + 1
            mat.append(accumulator)
            b = b + 1
        multiplied.append(mat)
        a = a + 1
    return multiplied
