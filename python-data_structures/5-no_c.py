#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for n in my_string:
        if n == 'c' or n == 'C':
            continue
        new += n
    return new
