#!/usr/bin/python3
"""
This module implements the add_integer function
Test for this module are contained in
./test/add-integer.txt file
The tests are pydoc test
feel free to addd some taste cases
"""


def add_integer(a, b=98):
    """
    adds two integers
    if one or both of the arguments are not int
    it raise a typeError exception
    """

    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
