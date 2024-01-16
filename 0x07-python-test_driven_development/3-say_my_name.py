#!/usr/bin/python3
"""
3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    prints the first and last name of person

    Args:
        first_name: the firstname
        last_name : the lastname

    Returns: None
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
