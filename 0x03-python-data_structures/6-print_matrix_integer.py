#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
        return
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end=(" " if i < len(row) - 1 else "\n"))
