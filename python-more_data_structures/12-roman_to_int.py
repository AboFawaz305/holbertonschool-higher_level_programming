#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_value = {
        "": 9999,
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    for c in roman_string:
        if c not in roman_value.keys():
            return 0
    for c in "MCXI":
        if roman_string.count(c) > 4:
            return 0
    for c in "DLV":
        if roman_string.count(c) > 1:
            return 0
    prev_char = ""
    total = 0
    for c in roman_string:
        if 1 < (roman_value[c] // roman_value[prev_char]) <= 10:
            total += -2 * roman_value[prev_char] + roman_value[c]
        elif roman_value[c] <= roman_value[prev_char]:
            total += roman_value[c]
        else:
            return 0
        prev_char = c
    return total
