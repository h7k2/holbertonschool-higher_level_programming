#!/usr/bin/python3
"""
Module 4-square
Defines a class Square with size validation, getter, setter, and area computation
"""


class Square:
    """
    Class Square that defines a square by its size
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default = 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size  # utilise le setter pour centraliser la validation

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
