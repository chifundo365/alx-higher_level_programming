#!/usr/bin/python3
"""
Takes i a URL and an email and send a POST request with the email passed as a parameter
Displays the body of the response, decoded in utf-8
"""
import urllib
import sys


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8')
