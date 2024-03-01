#!/usr/bin/python3
""" This module contains a locked class """


class LockedClass:
    """ class only allows last_name attribute """

    def __setattr__(self, key, value):
        if key == 'first_name':
            self.__dict__[key] = value
        else:
            msg = f"'LockedClass' object has no attribute '{key}'"
            raise AttributeError(msg)

    def __getattribute__(self, name):
        if name == 'first_name':
            return object.__getattribute__(self, name)
        else:
            msg = f"'LockedClass' object has no attribute '{name}'"
