#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays the body of the response
handels HTTPError
"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code > 399:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
