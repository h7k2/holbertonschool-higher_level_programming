#!/usr/bin/python3
"""
matrix division module
"""

def matrix_divided(matrix, div):
    """ divide all values """
    if type(matrix) is not list:
        raise Typeerror("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be number")
    if div == 0:
        raise ZeroDivisionerror("division by zero")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row must be the same size")
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(e / div, 3) for e in row] for row in matrix]
