#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = [list(row) for row in matrix]
    for i in range(len(matrix_copy)):
        for x in range(len(matrix_copy[i])):
            matrix_copy[i][x] **= 2
    return matrix_copy
