#!/usr/bin/python3
"matrix division"

def matrix_divided(matrix, div = "0"):
    "divide elements"
    if type(matrix) != list:
        raise TypeError("matrix must matrix of int/float")
    for r in matrix:
        if type(r) != list:
            raise TypeError("matrix must be a list")
    if div == 0:
        raise ZeroDivisionerror("division by 0")
    if not isinstance(div, int or float):
        raise TypeError("div must be number")

    size = len(matrix[0])
    for line in matrix:
        if len(line) is not size:
            raise TypeError("rows different size")
        for e in line:
            if type(e) not in (int):
                raise TypeError("matrix wrong type")

    new = []
    for row in matrix:
        new.append([round(e/div, 5) for e in row])
    return new
