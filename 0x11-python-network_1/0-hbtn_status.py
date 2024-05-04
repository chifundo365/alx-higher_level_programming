#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    _bytes = res.read()
    print('\t- type: {}'.format(type(_bytes)))
    print('\t- content: {}'.format(_bytes))
    print('\t- utf8 content: {}'.format(_bytes.decode('utf-8')))
