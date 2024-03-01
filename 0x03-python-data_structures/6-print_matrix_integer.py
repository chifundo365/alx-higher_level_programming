#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for e in matrix:
            lst_idx = len(e) - 1
            if (isinstance(e, list)):
                for x in e:
                    idx = e.index(x)
                    print("{:d}".format(x), end=" " if idx != lst_idx else "")
                print("")
