#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    list_copy = []
    for d in my_list:
        if d not in list_copy:
            list_copy.append(d)
            total += d
    del list_copy
    return total
