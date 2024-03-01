#!/usr/bin/python3
"""
Defines a Base class 'BaseGeometry'
"""


class BaseGeometry:
    """ Geometry  base class """

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
