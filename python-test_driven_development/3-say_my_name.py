#!/usr/bin/python3
"""
say my name module
"""

def say_my_name(first_name, last_name=' '):
    """print my name"""
    if type(first_name) != str:
        raise Typeerror("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("lastname must be a string")

    print("My name is {}{}".format(first_name, last_name))
