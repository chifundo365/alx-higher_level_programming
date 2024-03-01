#!/usr/bin/python3
"""
Defines a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Implements the a class representing a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.__x,
            self.__y,
            self.width
        )
