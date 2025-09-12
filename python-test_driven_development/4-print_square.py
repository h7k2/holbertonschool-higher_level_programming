#!/usr/bin/python3
"""
This module defines `print_square` to print a square with the character #.
It validates that size is a non-negative integer.
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size: the length of the square side (int)

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
