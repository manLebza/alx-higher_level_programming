#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ class that defines a square from Rectangle class """
    
    def __init__(self, size):
        """ method initializes a square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init(self.__size, self.__size)

    def area(self):
        """ method returns a string with the area """
        return super().area()
