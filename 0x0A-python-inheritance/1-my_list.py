#!/usr/bin/python3
"""
Implements MyList class
"""


class MyList(list):
    """
    Inherits from list class
    """

    def print_sorted(self):
        """
        prints a a list in ascending order

        Args:
            self: the instance itself

        Returns: None
        """
        print(sorted(self))
