#!/usr/bin/python3
"""
Contains a class that inherits from int
"""


class MyInt(int):
    """
    Inherits from int class and inverts == and != operators
    """

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
