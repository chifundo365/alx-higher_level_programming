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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes json string representation to a file

        Args:
            list_obj (list): list of instance object of square or rectangle
                             classes
                             if list is a empty it add an empty list
        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        dict_list = []
        for object in list_objs:
            dict_list.append(object.to_dictionary())
        with open(filename, "w") as file:
            file.write(Base.to_json_string(dict_list))
