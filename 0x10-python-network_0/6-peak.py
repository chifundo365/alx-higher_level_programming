#!/usr/bin/python3
""" Contains a function used to find a peak """


def find_peak(list_of_integers):
    """ finds the peak using a custom binary search algolithm """
    if not list_of_integers:
        return None

    def helper(start, end):
        if start == end:
            return list_of_integers[start]
        middle = (start + end) // 2
        if list_of_integers[middle] > list_of_integers[middle + 1]:
            return helper(start, middle)
        else:
            return helper(middle + 1,  end)
    return helper(0, len(list_of_integers) - 1)
