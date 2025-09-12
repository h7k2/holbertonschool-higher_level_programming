#!/usr/bin/python3
"""
This module defines `text_indentation` to print a text
with two new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?' and ':'.

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chunk = ""
    for ch in text:
        chunk += ch
        if ch in ".?:":
            print(chunk.strip())
            print()
            chunk = ""
    if chunk.strip():
        print(chunk.strip(), end="")
