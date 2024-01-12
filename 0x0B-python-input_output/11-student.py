#!/usr/bin/python3
"""
11-student.py
"""


class Student:
    """
    student classs with first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        makes a dictionary of all attributes in a class

        Args:
            self: the instance itsself
            attrs: attributes

        Return: a json serialisable python object with values equal:
                to the attributes in attrs or all if attr is None
         """
        obj = self
        if hasattr(obj, '__dict__'):
            new_dict = obj.__dict__.items()
            if attrs is not None:
                return {k: v for k, v in new_dict if k in attrs}
            return {k: v for k, v in new_dict}

    def reload_from_json(self, json):
        """
        replaces all attributes of the instance with a json str. attr.
        Args:
            json_string: json string containing attributes
            self       : the instance itself
        """
        self.__dict__ = json.loads(json)
