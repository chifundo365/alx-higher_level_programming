#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), file=sys.stderr)
        return True
    except (TypeError, ValueError):
        return False
