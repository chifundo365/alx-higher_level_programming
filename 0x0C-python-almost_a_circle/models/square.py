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

    @property
    def size(self):
        """
        Getter method for the size property

        Returns:
            int: the size property
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter: sets the value of the size

        Args:
            size: the size of the square

        Returns:
            None
        """
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    def update(self, *args, **kwargs):
        """
        updates the instance attributes

        Args:
            args (tuple): non-word arguments to update the attributes
            kwargs (dictionary): keyword arguments to update the attributes

        Returns:
            None
        """

        if len(args):
            if len(args) >= 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                    self.height = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) >= 4:
                    self.y = args[3]

        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.width = kwargs.get("size")
                self.height = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
