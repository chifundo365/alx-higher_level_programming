#!/usr/bin/python3
""" Contains Definition of load_from_json_file. """


def load_from_json_file(file_name):
    """" loads a file from json and coverts it to python object
    Args:
        file_name: file name of the json object
    Return: real python Object file
    """
    import json
    with open(file_name, encoding="utf-8") as f:
        return json.loads(f.read())
