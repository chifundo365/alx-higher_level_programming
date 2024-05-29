#!/usr/bin/python3
"""
Takes in an URL, sends a request to the url, displays the body response
Manages httpsError codes and displays the error code
"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            html = res.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
