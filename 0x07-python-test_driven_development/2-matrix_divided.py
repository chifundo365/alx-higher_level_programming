#!/usr/bin/python3
"""
2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix with a given input number

    Args:
        matrix: the input matrix to be divided by the given number
           div: the input number to be used as a divisor of the matrix

    Raises:
        TypeError: if the matrix is not a list of lists of integers.
                   if the row of the matrix arew not the same size.
                   if div is not a number

        ZeroDivisionError: if trying to divide by zero

    Returns: a new matrix with the quotients
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error_msg)
    prev_len = None
    for list_item in matrix:
        if not isinstance(list_item, list):
            raise TypeError(error_msg)
        if prev_len:
            if len(list_item) != prev_len:
                msg = "Each row of the matrix must have the same size"
                raise TypeError(msg)
        prev_len = len(list_item)
        for item in list_item:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(error_msg)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div <= 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(v / div, 2) for v in row] for row in matrix]
    return new_matrix
