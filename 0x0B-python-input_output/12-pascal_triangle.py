#!/usr/bin/python3
"""Creates a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n. """
    if n <= 0:
        return []

    triangl = [[1]]
    while len(triangl) != n:
        tri = triangl[-1]
        tmp = [1]
        for indx in range(len(tri) - 1):
            tmp.append(tri[indx] + tri[indx + 1])
        tmp.append(1)
        triangl.append(tmp)
    return triangl
