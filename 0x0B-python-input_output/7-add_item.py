#!/usr/bin/python3
""" add all arguments to a list
    coverts the list to a json object
    saves it to add_item.json file
"""


from sys import argv
import json
from os.path import exists
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
argv_length = len(argv)

if exists(filename):
    with open(filename, "r") as f:
        read_text = f.read()
        if read_text == "":
            save_to_json(argv[1:], filename)
        else:
            new_content = load_from_json_file(filename) + argv[1:]
            save_to_json(new_content, filename)
else:
    with open(filename, "w") as f:
        save_to_json(argv[1:], filename)
