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
        if list_objs:
            for object in list_objs:
                dict_list.append(object.to_dictionary())
        with open(filename, "w") as file:
            file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        convert JSON string representation to a list object

        Args:
            json_string: json string input to be converted back
                         to a list object

        Returns:
            list: list of JSON string representation of "json_string"
        """
        import json
        if json_string is not None:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        create a new instance with all the atrributes already set

        Args:
            dictionary (dict): a dictionary containing all the
                               attributes and their values
        Returns:
            Rectangle: a rectangle instance if the dictionary
                       contains rectangle attributes
            Square   : a Square instance if the dictonary input has
                       Square class attributes
        """
        new_instance = None

        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Finds a list of instances in a json file

        Returns:
            list: a  list of instance in the json file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                return cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
