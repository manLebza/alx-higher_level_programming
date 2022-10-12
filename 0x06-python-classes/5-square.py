#!/usr/bin/python3
class Square:
    """ class that defines a square by size.
    """
    def __init__(self, size = 0):
        """ method to initialise the square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be of integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ method that returns the square area of the object.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ method returns size of the square value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ method to set size value of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ method that prints a # square according to size  value
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end = '')

                print()
