#!/usr/bin/python3
"""
Implements a class named Rectangle which inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """ Implementation of a class reprsenting a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise the Rectangle object

        Args:
            height (int): height of the rectangle
            width  (int): width of the rectangle
            x      (int): x attribute of the rectangle
            y      (int): y attribute of the retangle
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets the width of the rectanglr

        Returns:
        int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        set the width of the rectangle to a value

        Returns:
        None
        """
        self.__width = width

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
        int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets the height of the rectangle to a value

        Returns:
        None
        """
        self.__height = height

    @property
    def x(self):
        """
        Gets the x of the rectangle

        Returns:
        int: x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        set the x of the rectangle to a value

        Returns:
        None
        """
        self.__x = x

    @property
    def y(self):
        """
        Gets the y of the rectanglr

        Returns:
        int: y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        set the y of the rectangle to a value

        Returns:
        None
        """
        self.__y = y
