#!/usr/bin/python3
"""
Defines a Base class 'BaseGeometry'
"""


class BaseGeometry:
    """ Geometry  base class """

    def area(self):
        """
        raises an exception message

        Args:
            self: the instance itself
        raises:
            ValueErrror: always

        Returns: None
        """
        raise Exception("area() is not implemented")
