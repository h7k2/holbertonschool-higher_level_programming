#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
"""append a string to a UTF-8 text file and return number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
