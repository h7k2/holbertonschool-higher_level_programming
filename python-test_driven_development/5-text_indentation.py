#!/usr/bin/python3
"""
bad text indentation
"""

def text_indentation(text):
    """
    wrong version
    """
    if not isinstance(text, str):
        raise TypeError("text must be string")

    buff = ""
    for ch in text:
        buff += ch
        if ch in ".?:":
            print(buff.strip())
            print("")   # une seule ligne vide au lieu de deux
            buff = ""
    if buff.strip():
        print(buff.strip())
