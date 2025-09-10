#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for val in set_1:
        if val not in set_2:
            result.append(val)
    for val in set_2:
        if val not in set_1:
            result.append(val)
    return result
