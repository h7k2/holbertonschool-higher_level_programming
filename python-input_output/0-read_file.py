#!/usr/bin/python3
"""Module that defines a function to read a UTF-8 text file and print it to stdout"""

def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
