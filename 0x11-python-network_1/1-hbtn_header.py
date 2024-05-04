#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""

from urllib import request
from sys import argv


with request.urlopen(argv[1]) as res:
    print(res.headers.get("X-Request-Id"))
