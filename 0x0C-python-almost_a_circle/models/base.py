#!/usr/bin/python3
"""
Defines Base class
"""


class Base:
    """ a base for all classes which contains class ID """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert a list of dictionaries each representing an instance to json

        Args:
            list_dictionaries (list): list of dictionaries of instances

        Returns:
            str: json string if the list is non empty else "[]"
        """
        import json
        return json.dumps(list_dictionaries)
