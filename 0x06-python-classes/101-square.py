#!/usr/bin/python3
"""define a class named Square with str magic function."""


class Square:
    """A class with a private attribute and a public method"""

    def __init__(self, size=0, pos=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        msg = "position must be a tuple of 2 positive integers"
        if type(pos) != tuple or len(pos) != 2:
            raise TypeError(msg)
        for x in pos:
            if type(x) != int or x < 0:
                raise TypeError(msg)
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
        return self.__position

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or len(value) != 2:
            raise TypeError(msg)
        for x in self._position:
            if type(x) != int or x < 0:
                raise TypeError(msg)
        self.__position = value

    def area(self):
        return self.__size ** 2

    def __str__(self):
        output = ''
        if self.__size == 0:
            output += "\n"
        elif self.__size > 0:
            for n in range(self.__position[1]):
                output += '\n'
            for i in range(self.__size):
                output += " " * self.__position[0]
                output += "#" * self.__size + "\n"
        return output

    def my_print(self):
        if self.__size == 0:
            print("")
        elif self.__size > 0:
            for n in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
