#!/usr/bin/python3
""" module function returns the number of lines
    of a text file.
"""

def number_of_lines(filename = ""):
    """ function reads from a file and prints the number of lines

    args:
        filename: filename

    Raises:
        Exception: when the file can be open
    """

    n_lines = 0
    with open(filename, 'r', encoding ="utf-8") as f:
        for line in f:
            n_lines += 1
    return n_lines
