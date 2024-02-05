#!/usr/bin/python3
"""
Defines inherits_from function to find if an object is a subclass
"""


def inherits_from(obj, a_class):
    """
    finds if an object is subclass of given class

    Args:
        obj: The object to be checked if it is a subclass of a given class
        a_class: input class object
    """
    return issubclass(obj, a_class)
