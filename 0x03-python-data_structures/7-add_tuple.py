#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if a_len >= 2 and b_len >= 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    list_a = [0, 0]
    list_b = [0, 0]
    if a_len == 1:
        list_a[0] = tuple_a[0]
    if b_len == 1:
        list_b[0] = tuple_b[0]
    if a_len >= 2:
        list_a = list(tuple_a[:2])
    if b_len >= 2:
        list_b = list(tuple_b[:2])
    tuple_sum = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    return tuple(tuple_sum)
