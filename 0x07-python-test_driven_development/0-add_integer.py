#!/usr/bin/python3
"""
this module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """ function adds two integers and/or a float type
    args:
        a: frist num
        b: second num

    Returns:
        the addition of two given numbers

    Raises:
    TypeError: if 'a' or 'b' are not integers or float types
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
