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
        """
        Setter for the size of the square.

        Args:
            value (int): new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the current square area.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
