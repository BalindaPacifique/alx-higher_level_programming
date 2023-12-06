#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = matrix.copy()

    for elemnts in range(len(matrix)):
        New_matrix[elemnts] = list(map(lambda x: x**2, matrix[elemnts]))

    return New_matrix
