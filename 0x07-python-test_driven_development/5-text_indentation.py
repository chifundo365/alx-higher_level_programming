#!/usr/bin/python3
"""
5-text_indentation
"""


def text_indentation(text):
    """
    prints text and print 2 newlines after either ',', ':' or '?'

    Args:
        text: The input text to print

    Raises:
        TypeError: if the input is not a string

    Returns: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newline = False
    for c in text:
        if text.index(c) == 0 and c.isspace():
            newline = False
            continue
        if newline and c.isspace():
            newline = False
            continue
        print(c, end="")
        newline = False
        if c in {":", ".", "?"}:
            print("\n")
            newline = True
