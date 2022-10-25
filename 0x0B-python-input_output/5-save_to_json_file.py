#!/usr/bin/python3
""" module writes an object to a text file using
    a JSON rep.
"""

import json

def save_to_json_file(my_obj, filename):
    """ function writes an object to text file
        by a JSON rep.

    args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when object can't be encoded
    """

    with open(filename, 'w', encoding = "utf-8") as f:
        json.dump(my_obj, f)
