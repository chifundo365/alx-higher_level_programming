#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return None
        big_int = 0
        for d in my_list:
            if isinstance(d, int):
                if d > big_int:
                    big_int = d
        return big_int
