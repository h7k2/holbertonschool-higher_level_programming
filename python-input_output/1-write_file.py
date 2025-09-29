#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return number of characters"""
    with open(filename, "w", encoding utf -8) as f:
        return f.write(text)
