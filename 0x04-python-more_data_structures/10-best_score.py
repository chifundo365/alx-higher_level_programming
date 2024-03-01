#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = max(v for v in a_dictionary.values())
    key = [k for k in a_dictionary.keys() if a_dictionary[k] == biggest]
    return key[0]
