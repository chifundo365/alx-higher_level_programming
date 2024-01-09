#!/usr/bin/python3
"""
This module implements the add_integer function
Test for this module are contained in
./test/add-integer.txt file
"""


def add_integer(a, b=98):
    """
    adds two integers raises an exception if fails
    """

    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
