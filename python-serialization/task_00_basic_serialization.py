#!/usr/bin/python3
"""adds the functionality to serialize a Python dictionary to a JSON file"""
import json


def serialize_and_save_to_file(data, filename):
    if not isinstance(data, dict):
        raise TypeError

    with open(filename, "w", encoding "utf-8") as f:
        json.dump(data, file, indent=2, ensure_ascii=False)

def load_and_deserialize(filename):
    with open(filename, "r", encoding "utf-8") as f:

    json.load(file)

    if not(dict)
        raise TypeError