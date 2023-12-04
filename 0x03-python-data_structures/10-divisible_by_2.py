#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_2 = []
    if my_list:
        for numbers in my_list:
            list_2.append(False if numbers % 2 else True)
        return list_2
