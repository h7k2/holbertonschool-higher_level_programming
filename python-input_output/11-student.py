#!/usr/bin/python3
"""Module defining the Student class with serialization and deserialization."""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
