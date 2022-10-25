#!/usr/bin/python3
class BaseGeometry:
    """ Class the defines the attributes of Geometric shapes """
    
    def area(self):
        """ Method that defines the area of geomtric shape """
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method recieves the value property
        args:
            name: name of object
            value: value of property

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
