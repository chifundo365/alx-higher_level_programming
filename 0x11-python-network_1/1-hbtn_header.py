#!/usr/bin/python3
"""
Sends a request to an URL and displays the value of a header variable
"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as res:
    for k, v in res.headers.items():
        if k == "X-Request-Id":
            print(v)
