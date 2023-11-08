#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        inner = []
        for j in i:
            inner.append(j * j)
        new.append(inner)
    return new
