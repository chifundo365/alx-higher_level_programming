#!/usr/bin/python3
"""
Defines a Base class 'BaseGeometry'
"""


class BaseGeometry:
    """ Geometry  base class """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        raises an exception with a messsage
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the int value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
