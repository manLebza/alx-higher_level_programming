#!/usr/bin/python3
""" module contains a function that returns the JSON,
    representation of the object
"""
import json

def to_json_stringg(my_obj):
    """ function returns the JSON rep. of an object

    args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
