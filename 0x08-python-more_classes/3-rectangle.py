#!/usr/bin/python3
"""
this module is composed by a class that defines a rectangle

"""
class Rectangle:
    """Class that defines a rectangle
    """
    def __init__(self, width = 0, height = 0):
        """method the  initialises the instance

        args:
            width: the width of the rectangle
            height: the height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method returns the value of the width
        Returns: rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """method defines the width
        args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method defines the value of the height
        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """method defines the height
        args:
            value: height

        Raise:
        TypeError: if height is not integer
        ValueError: if height is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle
        Returns: rrect. area
        
        """
        return self.width * self.height

    def perimeter(self):
        """method calculate the rect. perimeter
        returns:
            rectangle perimeter

        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height

    def __str__(self):
        """method returns a rect. #
        returns:
            str of the rect.

        """
        rectangle = " "

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]
