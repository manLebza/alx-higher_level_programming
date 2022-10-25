#!/usr/bin/python3
""" module contains a function that returns an object
    by a JSON representation.
"""
import json

def from_json_string(my_str):
    """ function returns an object by a json rep.

    args:
        my_str: JSON string representation

    Raises:
        Exception: when string can't be decoded
    """

    return json.loads(my_str)
