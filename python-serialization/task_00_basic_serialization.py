#!/usr/bin/env python3
"""adds the functionality to serialize a Python dictionary to a JSON file."""
import json


def serialize_and_save_to_file(data, filename):
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_and_deserialize(filename):
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)

    if not isinstance(obj, dict):
        raise TypeError("this does not contain a dictionary")

    return obj
