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
            self.x,
            self.y,
            self.width
        )

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
