#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len(tuple_a) == 0 and len(tuple_b) > 0:
        return (tuple_b[0:2])
    elif len(tuple_b) == 0 and len(tuple_a) > 0:
        return (tuple_a[0:2])
    else:
        return (0)
