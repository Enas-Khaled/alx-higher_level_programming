#!/usr/bin/python3
''' module  is instance '''


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified class ; otherwise False"""

    return type(obj) == a_class
