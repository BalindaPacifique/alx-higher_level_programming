#!/usr/bin/python3
"""Creates a class-checking function"""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class
        obj (any): object to check
        a_class (type): class to match the type of obj
    Returns:
        If obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
