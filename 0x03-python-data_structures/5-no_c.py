#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for elment in my_string:
        if elment != "c" and elment != "C":
            new_str += elment
    return new_str

