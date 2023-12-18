#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elemnts = 0
    for indx in range(x):
        try:
            print("{}".format(my_list[indx]), end="")
            elemnts += 1
        except IndexError:
            break
    print("")
    return (elemnts)
