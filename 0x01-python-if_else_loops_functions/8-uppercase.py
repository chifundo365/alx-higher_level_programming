#!/usr/bin/python3
def uppercase(str):
    newline = ''
    for i in range(len(str)):
        if i == len(str) - 1:
            newline = '\n'
        ascii_value = ord(str[i])
        if ascii_value >= 97 and ascii_value <= 122:
            upper_case = chr(ascii_value - 32)
            print("{}{}".format(upper_case, newline), end="")
        else:
            print("{}{}".format(str[i], newline), end="")
