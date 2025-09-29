#!/usr/bin/python3
"""a function that creat an python object with a json file."""
import json


def load_from_json_file(filename):
    """creat an python object with a json file."""
    with open(filename, "r", encoding="utf-8") as f:
       return json.load(f)
