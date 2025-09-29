#!/usr/bin/python3
"""a class Student that defines a studen"""


class student:
    """defines a student."""

    def __init__(self, first_name, last_name, age):
        """new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def json(self):
        """representation of a Student instance"""
        return self.__dict__
