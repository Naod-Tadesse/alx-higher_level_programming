#!/usr/bin/python3
"""the matrix dividing function"""


def matrix_divided(matrix, div):
    """this function divides every element in the matrix"""

    new_mat = []
    if not (isinstance(matrix, list)) or matrix == []:
        raise TypeError(
                "matrix must be a matrix (list of lists) of ""integers/floats"
                )
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                    )
        for element in item:
            if not (isinstance(element, float) or isinstance(element, int)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    for item in matrix:
        if not (len(item) == len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")

    if not (type(div) == int) and not (type(div) == float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for item in matrix:
        new_mat.append([round(element / div, 2) for element in item])
    return new_mat
