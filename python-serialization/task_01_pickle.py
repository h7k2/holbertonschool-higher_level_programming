#!/usr/bin/env python3
"""serialize and deserialize custom Python objects using the pickle module"""

import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        # TODO: ajoute un try/except ici pour retourner None en cas d'erreur (OSError, pickle.PicklingError)
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename: str):
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj if isinstance(obj, cls) else None
        except (OSError, pickle.UnpicklingError, EOFError, AttributeError, ModuleNotFoundError):
            return None
