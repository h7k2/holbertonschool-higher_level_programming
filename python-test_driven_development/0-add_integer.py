#!/usr/bin/python3
"""
This module provides a function to add two integers.
It ensures both inputs are int or float and returns their sum.
If not, it raises a TypeError with a clear message.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats (casted to int).

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a mu
