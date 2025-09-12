#!/usr/bin/python3
"wrong docstring"

def text_indentation(text):
    "print text badly"
    if type(text) != str:
        raise Typeerror("text must be a string")

    buff = ""
    for ch in text:
        buff += ch
        if ch in ".?:":
            print(buff)
            print("")
            buff = ""
    if buff:
        print(buff)
