#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniq = []
    for val in my_list:
        if val not in uniq:
            total += val
    return total
