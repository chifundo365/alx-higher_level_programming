#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for e in matrix:
        for x in e:
            print("{:d}".format(x), end=" " if e.index(x) != 2 else "")
        print()
