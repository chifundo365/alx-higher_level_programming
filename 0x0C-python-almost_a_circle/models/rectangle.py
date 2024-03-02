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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        if height < 1:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
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
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        find the area of the rectangle

        Returns:
        int: area of the rectangle
        """
        return (self.__width) * (self.__height)

    def update(self, *args, **kwargs):
        """
        Updates instance attributes using keyword and non-keyword arguments:

        Args:
            args (tuple): arguments to update the attributes
            kwargs (dict): keyword arguments to update the instance attribute

        Returns: None
        """
        if len(args) >= 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        else:
            if len(args):
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        if not len(args):
            if len(kwargs):
                if "id" in kwargs:
                    self.id = kwargs.get("id")
                if "width" in kwargs:
                    self.__width = kwargs.get("width")
                if "height" in kwargs:
                    self.__height = kwargs.get("height")
                if "x" in kwargs:
                    self.__x = kwargs.get("x")
                if "y" in kwargs:
                    self.__y = kwargs.get("y")

    def display(self):
        """
        prints to stdout the rectangle instance with the character #
        prints the # relative to the width, height and x, y cordinates

        Returns:
        None
        """
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """
        Creates a dictionary with the instance attributes created inside class

        Returns:
            dict: dictionary containing id, width, height, x and y attributes
        """
        new_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return new_dict

    def __str__(self):
        """
        modifies the string value of the rectangle class

        Returns:
            str: (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
