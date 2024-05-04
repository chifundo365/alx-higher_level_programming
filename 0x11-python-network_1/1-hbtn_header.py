#!/usr/bin/python3
""" 
Sends a request to an URL and displays the value of a header variable

This script takes a URL as a command-line argument and sends a request to that URL. It then searches
for a specific header variable, 'X-Request-Id', in the response headers and prints its value.

Usage:
    python3 script_name.py <url>

Example:
    python3 script_name.py http://example.com

Dependencies:
    This script requires Python 3, sys module and the urllib module.
"""

from urllib import request
from sys import argv


with request.urlopen(argv[1]) as res:
    for k, v in res.headers.items():
        if k == "X-Request-Id":
            print(v)
