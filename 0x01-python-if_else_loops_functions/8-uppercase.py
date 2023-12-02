#!/usr/bin/python3
def uppercase(str):
    newline = ''
    ascii_value = 0
    for i in range(len(str) + 1):
        if str:
            s = str[i]
        else:
            s = ""
        if i == len(str) - 1 or i == len(str):
            newline = '\n'
        if str:
            ascii_value = ord(s)
        if ascii_value >= 97 and ascii_value <= 122:
            upper_case = chr(ascii_value - 32)
            print("{}{}".format(upper_case, newline), end="")
        else:
            print("{}{}".format(s, newline), end="")
        if newline == '\n':
            break
(uppercase(""))
