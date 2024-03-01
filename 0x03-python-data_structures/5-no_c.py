#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        new_string = ""
        for s in my_string:
            if s != 'c' and s != 'C':
                new_string += s
        return new_string
