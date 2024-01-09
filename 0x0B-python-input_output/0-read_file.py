#!/usr/bin/python3
"""" implements a function to read a file"""


def read_file(filename=""):
    """ read a file using utf-8 encoding
    Args:
        filename: the name of the file to read
    Return: Nothing
    """
    with open(filename) as f:
        contents = f.read()
        print(contents, end="")
