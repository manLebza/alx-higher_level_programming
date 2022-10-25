#!/usr/bin/python3
""" module returns the dictionary description with a simple
    data structure for a JSON serialisation of the object
"""

def class_to_json(obj):
    """ function returns the dict. description of an object. """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()

    return res
