#!/usr/bin/python3
class Square:
    """ class that defines a square by its size.
    """
    def __init__(self, size = 0):
        """ Method to initialise the square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """ Method that returns the square area of the object.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to return the size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set size value of square object.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError(" size must be >= 0")
        else:
            self.__size = value
