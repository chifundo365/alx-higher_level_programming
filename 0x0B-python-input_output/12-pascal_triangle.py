#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """
    makes a pascals triangle
    Args:
        n: number of rows for the triangle
    Return: a list of lists of int's representing pasclas triangle
    """
    if (n <= 0):
        return []
    array = []
    for row in range(n):
        if row == 0:
            array.append([1])
            prev = [1]
        else:
            length = len(prev)
            current = []
            current.append(1)
            for col in range(length - 1):
                pos = length - col - 1
                if pos:
                    pos_value = prev[col] + prev[col + 1]
                    current.append(pos_value)
            current.append(1)
            prev = current
            array.append(current)
    return array
