#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rows in range(len(matrix)):
            for row_item in range(len(matrix[rows])):
                if row_item != len(matrix[rows]) - 1:
                    endsp = ' '
                else:
                    endsp = ''
                print("{:d}".format(matrix[rows][row_item]), end=endsp)
            print()
