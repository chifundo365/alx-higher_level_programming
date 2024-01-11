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

    if (type(obj) == dict) and (hasattr(obj, '__dict__')):
        allowed = int, str, dict, list, bool
        s_obj = {k: v for k, v in obj.items() if isinstance(v, allowed)}
        return s_obj
