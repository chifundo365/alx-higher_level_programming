#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = max(v for v in a_dictionary.values())
    return (key[0] for key in a_dictionary.keys() if a_dictionary[key] == biggest)
