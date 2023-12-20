#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except(TypeError, ValueError):
        msg = "Exception: Unknown format code 'd' for object of type"
        if value is None:
            print("{} 'None'".format(msg), file=sys.stderr)
            return False
        data_types = [int, float, list, str, bool, tuple, dict]
        for i in data_types:
            if isinstance(value, i):
                print("{} {}".format(msg, str(i)[7:12], file=sys.stderr))
        return False
