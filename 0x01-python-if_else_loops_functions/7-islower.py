#!/usr/bin/python3
"""This module checks for lowercase charactors in sequence."""


def islower(c):
    """Function checks for lowercase charactors."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
