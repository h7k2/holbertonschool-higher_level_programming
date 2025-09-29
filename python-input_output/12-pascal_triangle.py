#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows"""
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        prev = triangle[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
