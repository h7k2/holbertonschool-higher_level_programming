#!/usr/bin/python3
class BaseGeometry:
    def area(self)
        raise Exeption("area() is not implemented")

    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0
            raise ValueError(f"{name}must be greater than 0")
