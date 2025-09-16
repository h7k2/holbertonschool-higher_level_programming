#!/usr/bin/python3
"""Module 1-square
Defines a class Square with a private instance attribute: size"""


class Square:
    """Class Square that defines a square by its size"""

    def __init__(self, size):
          """Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value verification here)."""
        self.__size = size
