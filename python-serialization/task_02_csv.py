#!/usr/bin/env python3
"""Reading data from one format (CSV) and converting to JSON"""

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
