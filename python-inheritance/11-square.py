#!/usr/bin/python3
"""Square module that inherits from Rectangle and customizes __str__."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by a private size."""

    def __init__(self, size):
        """Initialize Square after validating size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation: [Square] <width>/<height>."""
        return f"[Square] {self.__size}/{self.__size}"
