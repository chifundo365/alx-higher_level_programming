#!/usr/bin/python3
"""
implements a function that finds if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Tells if an object is an instance of,
    or if the object is an instance of a class that inherited from

    Args:
        obj: input object to check if its an instance of 'a_class' or an \
        inherited from the 'a_class'
        a_class: class object to be checked to with 'obj'

    Returns: True - if the obj is an instance of a_class or inherits from it
             False - if obj is not an instance of a
             -class or if it doesnt inherit
    """
    return (isinstance(obj, a_class))
