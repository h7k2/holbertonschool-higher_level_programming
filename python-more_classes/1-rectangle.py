#!/usr/bin/python3
"""
Module 1-rectangle
Defines a Rectangle class with private width and height,
and property getters/setters with validation
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle by its width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): width of the rectangle (default = 0)
            height (int): height of the rectangle (default = 0)

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 0
        """
        self.width = width   # utilise le setter pour valider
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle
        Validates that width is an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle
        Validates that height is an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
