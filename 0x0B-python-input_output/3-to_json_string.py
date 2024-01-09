#!/usr/bin/python3
""" Contains a to_json_string. """


import json


def to_json_string(my_obj):
    """ converts an object to its Json representation
    Args:
        my_obj: object to be converted to json rep.
    Return: JSON representation string
    """
    return json.dumps(my_obj)
