#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for val in set_1:
        if val in set_2:
            result.append(val)
    return result