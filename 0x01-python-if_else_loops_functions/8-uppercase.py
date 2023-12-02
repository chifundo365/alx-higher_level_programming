#!/usr/bin/python3
def uppercase(str):
    if str:
        result = ''
        for i in range(len(str)):
            ascii_value = ord(str[i])
            if ascii_value >= 97 and ascii_value <= 122:
                result = chr((ascii_value - 32))
            else:
                result = str[i] 
            print("{}".format(result), end="")
    print("")
