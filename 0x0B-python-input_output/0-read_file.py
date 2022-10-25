#!/usr/bin/python3
""" Module contains a function which reads from a file """

def read_file(filename = ""):
    """ function reads from a file
    args:
        filename: filename

    Raises:
        Exception: when the file cant be opened
    """
    with open(filename, 'r', encoding = "utf-8") as f:
        read_data = f.read()
        print(read_data, end= '')
