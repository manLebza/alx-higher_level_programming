#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ function returns True/False if obj is instance of a_class
    args:
        obj: class object
        a_class: class type

    Returns:
        True  if obj is an instance of a class
        False, otherwise
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
