#!/usr/bin/python3
"""BaseGeometry module: defines a base class with validation helpers."""
 

class BaseGeometry:
    """BaseGeometry class: provides 'area' and 'integer_validator' helpers."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that 'value' is a strictly positive integer.

        Args:
            name (str): name used in error messages.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
