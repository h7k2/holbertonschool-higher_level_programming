#!/usr/bin/python3
"""
This module defines `say_my_name` to print a formatted string.
It validates that first_name and last_name are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Print: My name is <first name> <last name>.

    Raises:
        TypeError: if first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
