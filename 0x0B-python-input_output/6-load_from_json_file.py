#!/usr/bin/python3
""" module creates an object from a JSON file
"""
import json

def load_from_json_file(filename):
    """ function creates an object from a json file

    args:
        filename: textfile name

    Raises:
        Exception: when object can't be encoded
    """
    with open(filename, 'r', encoding = "utf-8") as f:
        return json.load(f)
