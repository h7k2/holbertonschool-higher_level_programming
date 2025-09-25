#!/usr/bin/env python3
"""VerboseList: list subclass that logs mutations."""

class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        items = list(iterable)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
