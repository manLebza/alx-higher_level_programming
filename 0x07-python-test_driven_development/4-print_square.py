#!/usr/bin/python3
"""
this module is composed by a function that prints a square with this char #
"""

def print_square(size):
    """function that prints a square with char #
    args:
        size: size of the square printed

    Returns: void

    Raises:
        TypeError: if size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
