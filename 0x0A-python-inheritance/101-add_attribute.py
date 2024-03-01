#!/usr/bin/python3
""" Defines the addd atrribute function """


def add_attribute(obj, name, value):
    """
    Adds a new attribute to object
    Args:
        obj: object to set the atrribute to
        name: name of the attribute to add
        value: The attribute value

    Raises:
        TypeError: if the attribute can not be added to the object
    Returns: None
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
