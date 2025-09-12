#!/usr/bin/python3
"""
This module defines `matrix_divided` to divide all elements of a matrix.
It validates the input matrix and the divisor with clear error messages.
It returns a new matrix with results rounded to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by `div`.

    Returns a new matrix with each value rounded to 2 decimals.
    Raises TypeError/ZeroDivisionError with the required messages.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(
        not all(isinstance(x, (int, float)) for x in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
