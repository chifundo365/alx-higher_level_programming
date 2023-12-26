#!/usr/bin/python3
"""Defines a Square class with a private object attribute"""


class Square:
    """Represents a square class"""

    def __init___(self, size=0):
        """Square class constructor method"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
