#!/usr/bin/env python3
"""eading data from one format (CSV)"""
import json
import CSV

def convert_csv_to_json(filename):
    with open(filename, "r", eading="utf-8") as csv.DictReader
     reader = csv.DictReader(csv_file)
            data = list(reader)
    
      with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
    
    return True

else 
    return False
