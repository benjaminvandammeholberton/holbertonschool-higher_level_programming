#!/usr/bin/python3
def roman_to_int(roman_string):
    romans_value = {"I": 1, "V": 5, "X": 10, "M": 1000, "D": 500,
                    "C": 100, "L": 50}
    result = 0
    prev_value = 0
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    for char in reversed(roman_string):
        if romans_value[char] < prev_value:
            result -= romans_value[char]
        else:
            result += romans_value[char]
        prev_value = romans_value[char]
    return result
