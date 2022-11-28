#!/usr/bin/python3
""" In this module the method lookup(obj)
returns a list of available attributes and
methods of an object in the lookup method.
"""


def lookup(obj):

    """This function returns a list of available
    attributes and methods of an object
    args:
    obj: instance of a class
    Returns:
    list of attributes"""

    return dir(obj)
