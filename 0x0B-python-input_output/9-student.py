#!/usr/bin/python3
"""
9-student.py
"""


class Student:
    """
    student classs with first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(self):
        """
        makes a dictionary of all attributes in a class

        Args:
            self: the instance itsself

        Return: a json serialisable python object with values equal to either
                int, str, bool, and dict
         """
        obj = self
        if hasattr(obj, '__dict__'):
            new_dict = obj.__dict__.items()
            allowed = int, str, bool, dict, list
            return {k: v for k, v in new_dict if isinstance(v, allowed)}
