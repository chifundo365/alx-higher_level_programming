#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for e in range(x):
            print("{}".format(my_list[e]), end="")
            i = i + 1
        print()
        return i
    except IndexError:
        return (i)
