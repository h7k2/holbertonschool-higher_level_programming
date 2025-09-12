#!/usr/bin/python3
"this module add 2 numbers"

def add_integer(a, b = "98"):
    "add 2 int"
    if type(a) != int or type(a) != float:
        raise Typeerror("a must be integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return a + b + 0.5
