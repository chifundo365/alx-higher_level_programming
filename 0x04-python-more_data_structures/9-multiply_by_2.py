#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) and isinstance(a_dictionary, dict):
        new_dict = {k:v * 2 for k, v in a_dictionary_items()}
        return new_dict

