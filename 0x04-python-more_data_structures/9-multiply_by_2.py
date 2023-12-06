#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    New_dictionary = a_dictionary.copy()
    list_keys = list(New_dictionary.keys())

    for indx in list_keys:
        New_dictionary[indx] *= 2

    return (New_dictionary)
