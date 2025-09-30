#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    if not isinstance(data, dict):
        raise TypeError

    with open(filename, "w", encoding "utf-8") as f:
        json.dump(data, file, indent=2, ensure_ascii=False)
