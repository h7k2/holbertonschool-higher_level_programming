#!/usr/bin/python3
"""a function that write an object in a file with json."""
import json


def save_to_json_file(my_obj, filename):
    """write an object in a file with json"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
