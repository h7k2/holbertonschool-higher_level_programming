#!/usr/bin/python3
"""
matrix divided module
"""

def matrix_divided(matrix, div):
    """divide each element by div"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix of int/float")
    if not isinstance(div, (int, float)):
        raise Typeerror("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row must be the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix of int/float")

    return [[round(e / div, 3) for e in row] for row in matrix]
