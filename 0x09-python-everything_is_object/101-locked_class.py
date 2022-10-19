#!/usr/bin/python3
"""
module contains a class that avoids dynamically created attributes
"""
class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """__init__ method"""
        pass
