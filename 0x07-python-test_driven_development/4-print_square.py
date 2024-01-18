#!/usr/bin/python3
"""
4-print_square.py
"""


def print_square(size):
    """
    prints specified number of squares with #

    Args:
        size: size of the square to print(width/height)

    Returns:
        None
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        print("#" * int(size))
