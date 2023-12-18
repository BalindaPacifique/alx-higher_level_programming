#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list
        x (int): The number of elements of my_list

    Returns:
        The number of elements printed.
    """
    elemnts = 0
    for indx in range(x):
        try:
            print("{}".format(my_list[indx]), end="")
            elemnts += 1
        except IndexError:
            break
    print("")
    return (elemnts)
