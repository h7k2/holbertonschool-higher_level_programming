#!/usr/bin/python3
"""a script that adds all arguments to a Python list"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

import os
if os.path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
    items = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
