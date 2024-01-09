#!/usr/bin/python3
""" Contains a save_to_json_file function. """


def save_to_json_file(my_obj, filename):
    """ saves a Json rep. to a  file.
    Args:
        my_obj  : object to be serialised
        filename: name of the file to save to
    Return: void
    """
    import json
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
