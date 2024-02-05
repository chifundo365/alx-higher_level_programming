#!/usr/bin/python3
"""
Implements is _same_class function
"""


def is_same_class(obj, a_class):
    """
    checks if object is an instance of the specfied class
    Args:
        obj: the object to check if is an instance of a_class
        a_class: class to be compared to the obj
    Returns:
        true - if the object is an instance of a_class
        false- f the object is not an instance of a_class
   """
    return issubclass(obj, a_class)
