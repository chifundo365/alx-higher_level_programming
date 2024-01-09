#!/usr/bin/python3
""" Contains a from_josn_string function. """


def from_json_string(my_str):
    """ it converts a JSON object to real python object.
    Arg:
        my_str: string representation of JSON object
    Return: real python object
    """
    import json
    return json.loads(my_str)
