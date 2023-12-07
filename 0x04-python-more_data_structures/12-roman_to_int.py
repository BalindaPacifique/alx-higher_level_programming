#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    #if roman_string is None or type(roman_string) != str:
        #return 0
    Roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [Roman_int[n] for n in roman_string] + [0]
    num = 0

    for indx in range(len(numbers) - 1):
        if numbers[indx] >= numbers[indx+1]:
            num += numbers[indx]
        else:
            num -= numbers[indx]

    return num
