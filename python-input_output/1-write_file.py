#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding utf -8) as f:
        print f.write(text)
