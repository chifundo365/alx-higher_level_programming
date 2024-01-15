#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates a pascal's triangle up to n rows

    Args:
        n (int): number of rows for the triangle

    Return: a list of lists of int's representing pasclas triangle
    """
    if (n <= 0):
        return []
    triangle = []
    for row in range(n):
        current_row = [1]  # triangle always starts with a 1
        if triangle:
            prev_row = triangle[-1]
            for col in range(len(prev_row) - 1):
                current_row.append(prev_row[col] + prev_row[col + 1])
            current_row.append(1)  # triangle always ends with a 1
        triangle.append(current_row)
    return triangle
