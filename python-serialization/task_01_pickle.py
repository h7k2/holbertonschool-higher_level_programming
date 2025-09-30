#!/usr/bin/env python3
"""serialize and deserialize custom Python objects using the pickle module"""

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
    self.name = name
    self.age = age
    self.is_student = is_student

    def display
        print()
        print()
        print()

    def serialize(self, filename):
        with open(filename, "wb") as f
            pickle.dump(self, f)

    def deserialize(cls, filename: str):
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj if isinstance(obj, cls) else None
        except (OSError, pickle.UnpicklingError, EOFError, AttributeError, ModuleNotFoundError):
            return None
