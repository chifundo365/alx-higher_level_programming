#!/usr/bin/python3
"""
100-append_after.py
"""


def read_all_lines(filename):
    """
    Reads all the lines of a file

    Args:
        filename: the name of the file to read

    Return:
            a list of strings of all the lines
    """
    with open(filename, "r") as f:
        read_lines = f.readlines()
    return read_lines


def write_all_lines(filename, content=[]):
    """
    write all the characters in content to a file

    Args:
        filename (str): name if the file to write to
        content (list): list of string containing the content

    Returns:
        None
    """
    total_written = 0
    with open(filename, "w") as f:
        string_to_write = ''.join(string for string in content)
        total_written = f.write(string_to_write)


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a string to a line after the searched string line

    Args:
        filename: name of the file to search and append the strings
        search_string: strng to be searched
        new_string: the string to be appended after the saeched string line

    Returns:
        None
    """
    read_lines = read_all_lines(filename)
    for i in range(len(read_lines)):
        if search_string in read_lines[i]:
            read_lines[i] = read_lines[i] + new_string + "\n"
    write_all_lines(filename, read_lines)
