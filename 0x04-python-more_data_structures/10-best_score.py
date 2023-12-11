#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary.values()) == 0:
        return None
    return (max(v for v in a_dictionary.values()))
