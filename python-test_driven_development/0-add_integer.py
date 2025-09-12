#!/usr/bin/python3
"""
add 2 int
"""

def add_integer(a, b=98):
    """add two numbers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise Typeerror("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + b
