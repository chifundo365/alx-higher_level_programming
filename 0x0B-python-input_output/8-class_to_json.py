#!/usr/bin/python3
""""
8-class_to_json
"""


def class_to_json(obj):
    """
    makes a dictionary of all attributes in a class

    Args:
        obj: the object

    Return: a json serialisable python object with values equal to either
            int, str, bool, and dict
    """
    if hasattr(obj, '__dict__'):
        new_dict = obj.__dict__.items()
        allowed = int, str, bool, dict
        return {k: v for k, v in new_dict if isinstance(v, allowed)}
