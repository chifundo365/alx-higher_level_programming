#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        msg = "Exception: Unknown format code 'd' for object of type"
        if value is None:
            print("{} 'None'".format(msg))
            return False
        data_types = [int, float, list, str, bool, tuple, dict]
        for data_type in data_types:
            if isinstance(value, data_type):
                p = data_type[7:12]
                print("{} {}".format(msg, p))
                break
        return False
