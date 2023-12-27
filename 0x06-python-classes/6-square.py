#!/usr/bin/python3
"""define a class named Square"""


class Square:
    """A class with a private attribute and a public method"""

    def __init__(self, size=0, pos=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(pos) != tuple or len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__postion

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            msg = "position must be a tuple of 2 positive integers"

            raise TypeError(msg)
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        elif self.__size > 0:
            if self.__position[1] != 1 and self.__position[0]:
                print(" " * self.__position, end='')
            for i in range(self.__size):
                print("#" * self.__size)
