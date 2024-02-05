#!/usr/bin/python3
"""
implements lookup function
"""


def lookup(obj):
    """
    finds the list of available attributes and methods of an object.
    Args:
        obj: The object to find the list of attributes and methods

    Returns: A list object
    """
    return dir(obj)
