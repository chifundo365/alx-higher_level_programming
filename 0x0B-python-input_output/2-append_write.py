#!/usr/bin/python3
""" contains 2-append_write function. """


def append_write(filename="", text=""):
    """ Appends data to a file (utf-8 encoding)
    Args:
        filename: the name of the file to write to
        text    : text to be written
    Return: number of characters read
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
