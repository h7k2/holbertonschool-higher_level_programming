#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self._it = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._it)
        return item

    def get_count(self):
        return self._count
