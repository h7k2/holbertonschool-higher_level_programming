#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_value = float('-inf')
    for key, val in a_dictionary.items():
        if val > best_value:
            best_value = val
            best_key = key
    return best_key