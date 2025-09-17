#!/usr/bin/python3
"""
Module 6-square
Defines a class Square with size, position, area computation,
and printing using '#' with spaces for position
"""


class Square:
    """
    Class Square that defines a square by its size and position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default = 0)
            position (tuple): The position offset (default = (0, 0))

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.
        Validates that size is an integer >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.
        Validates that position is a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#', considering position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()
