#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
uses the requests package
"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
