#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for val in a_dictionary.values():
        print(val, ":", a_dictionary)
    return a_dictionary.keys