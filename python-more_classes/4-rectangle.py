#!/usr/bin/python3
"""
Module 4-rectangle
Defines a Rectangle class with width, height,
area, perimeter, str and repr
"""


class Rectangle:
    """
    Class Rectangle that defines a rectangle by its width and height
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.heigth = height

    @property
    def width(self):
        return self.__widht

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "#" * self.__width

    def __repr__(self):
        return f"Rect({self.__width}, {self.__height})"
