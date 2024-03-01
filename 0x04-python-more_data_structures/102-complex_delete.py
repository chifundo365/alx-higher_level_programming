#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_be_deleted = {k: v for (k, v) in a_dictionary.items() if v == value}
    for key in to_be_deleted:
        del a_dictionary[key]
    return a_dictionary
