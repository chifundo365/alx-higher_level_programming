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
