#!/usr/bin/python3
"""
this module is composed by a function that prints a message
"""

def say_my_name(first_name, last_name = ""):
    """function prints "My name is <first name> <last name>"
    args:
        first_name: first name
        last_name: last name

    Returns: void

    Raises:
        TypeError: if first_name or last_name is not a string
    """

    if type(fist_name is not str:
            raise TypeError("first_name must be a string")

    if type(last_name) is not str:
            raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
