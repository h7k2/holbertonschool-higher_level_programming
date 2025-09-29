#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): text. Defaults to "".
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)