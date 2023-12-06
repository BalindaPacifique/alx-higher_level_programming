#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    Ordered_list = list(a_dictionary.keys())
    Ordered_list.sort()
    for indx in Ordered_list:
        print("{}: {}".format(indx, a_dictionary.get(indx)))
