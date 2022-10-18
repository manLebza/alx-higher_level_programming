#!/usr/bin/python3
"""
    this module is composed by class that defines a rectangle

"""
class Rectangle:
    """class defines a rectangle
    """

    def __init__(self, width = 0, height = 0):
        """method initialises the instance
        args:
            width: rect. width
            height: rect. height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method returns the value of thhe width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """method defines width
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
        """method returns the value of the height
        Returns:
            rectangle  height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """method defines the height

        args:
            value: height
        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that calculates the rectangle area
        Returns:
            rectangle area

        """
        return self.width * self.height
    
    def perimeter(self):
        """method that calculates the rectangle perimeter
        Returns:
            rectangle perimeter

        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """method that returns the rect #
        Returns:
            str of the rectangle

        """
        rectangle = " "

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width)

        return rectangle[:-1]

    def __repr__(self):
        """method that returns a string representation of instance
        Returns:
            string represantation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)
