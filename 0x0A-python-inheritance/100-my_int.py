#!/usr/bin/python3
"""
Contains a class that inherits from int
"""


class MyInt(int):
    """
    Inherits from int class and inverts == and != operators
    """


    def __eq__(self, other):
        if self == other:
            return False
        return True
    
    def __ne__(self, other):
        if self != other:
            return True
        return False
