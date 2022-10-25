#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ fuction returns True/False if is an instrance of a class
    args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """

    return isinstance(obj, a_class)
