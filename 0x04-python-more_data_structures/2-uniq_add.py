#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for d in my_list:
        if my_list.count(d) == 1:
            total += d
    return total
