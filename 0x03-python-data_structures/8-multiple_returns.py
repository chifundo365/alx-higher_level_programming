#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    first_char = None
    if str_len > 0:
        first_char = sentence[0]
    return str_len, first_char
