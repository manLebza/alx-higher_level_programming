#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class defines a rectangle from baseGeometry class """

    def __init__(self, width, height):
        """ initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method that returns the area of the instance """
        return self.__width * self.__height

    def __str__(self):
        """ special method that returns a printable string """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
