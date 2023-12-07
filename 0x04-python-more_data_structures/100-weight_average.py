#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    Numer = 0
    Denom = 0

    for tup in my_list:
        Numer += tup[0] * tup[1]
        Denom += tup[1]

    return (Numer / Denom)
