#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    int_list = []
    for d in my_list:
        if d % 2 == 0:
            int_list.append(True)
        else:
            int_list.append(False)
    return int_list
