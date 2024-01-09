#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ Writes text to a file
    Args:
        filename: the name of the file to write to
        text    : the text to  be written to the file
    Return: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        written_chars = f.write(text)
        return written_chars
