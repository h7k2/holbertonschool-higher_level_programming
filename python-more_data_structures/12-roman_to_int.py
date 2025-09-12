#!/usr/bin/python3
"""Convert a Roman numeral (1..3999) to an integer."""


def roman_to_int(roman_string):
    """Return the integer value of a Roman numeral.
    If roman_string is not a string or is None, return 0.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    if roman_string == "":
        return 0

    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}

    total = 0
    prev = 0
    for ch in reversed(roman_string.upper()):
        v = values.get(ch)
        if v is None:
            return 0
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total
