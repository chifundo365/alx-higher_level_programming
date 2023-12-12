#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == 0 or not roman_string:
        return 0
    roman_string = roman_string.upper()
    sum = 0
    key_numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
    prev_value = 0
    for rmn_char in roman_string:
        if rmn_char in key_numerals.keys():
            rmn_value = key_numerals[rmn_char]
            if rmn_value > prev_value and prev_value != 0:
                sum += rmn_value - (prev_value + prev_value)
            else:
                sum += rmn_value
            prev_value = rmn_value
    return sum
