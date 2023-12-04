#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    leng_a, leng_b = len(tuple_a), len(tuple_b)
    New_tuple = ((tuple_a[0] if leng_a >= 1 else 0) +
                 (tuple_b[0] if leng_b >= 1 else 0),
                 (tuple_a[1] if leng_a >= 2 else 0) +
                 (tuple_b[1] if leng_b >= 2 else 0))
    return New_tuple
