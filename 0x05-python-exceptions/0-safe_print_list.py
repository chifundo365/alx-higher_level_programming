#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[:x])
    except IndexError:
        i = 0
        for x in my_list:
            print("{}".format(x), end="")
            i++
        return i
    else:
        return x
