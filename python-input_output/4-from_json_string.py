#!/usr/bin/python3
"""a function that returns the JSON representation of an string."""
import json


def from_json_string(my_str):
     """return the JSON representation of a string"""
     return json.loads(my_str)
