#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == 0 or not roman_string:
        return 0
    roman_string = roman_string.upper()
    sum = 0
    key_numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }

    for rmn_char in roman_string:
        if rmn_char in key_numerals.keys():
            rmn_value = key_numerals[rmn_char]
            if roman_string.index(rmn_char) != 0 and rmn_value > sum:
                sum = rmn_value - sum
            else:
                sum += rmn_value
    return sum
