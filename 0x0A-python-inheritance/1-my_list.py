#!/usr/bin/python3
"""Module prints out list."""


class MyList(list):
    """ class inherits attribute references of a class list
    args:
    list: class list
    """

    def print_sorted(self):
        """ Method prints a sorted list """
        l_sorted = sef.copy()
        l_sorted.sort()
        print(l_sorted)
