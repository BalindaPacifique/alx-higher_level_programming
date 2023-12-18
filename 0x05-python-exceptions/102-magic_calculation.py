#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for indx in range(1, 3):
        try:
            if indx > a:
                raise Exception('Too far')
            result += a ** b / indx
        except Exception:
            result = b + a
            break
    return result
