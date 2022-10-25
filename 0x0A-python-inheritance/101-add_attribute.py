#!/usr/bin/python3
def add_attribute(obj, name, value):
    """ function adds a new attribute to an object

    args:
        obj: object to be added
        name: attribute name
        value: attribute value

    raises:
        TypeError: when attribute cant be added

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("cant add new attribute")
    setattr(obj, name, value)
