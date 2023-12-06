#!/usr/bin/python3
def search_replace(my_list, search, replace):
    changed_list = list(map(lambda n: replace if n == search else n, my_list))
    return (changed_list)
