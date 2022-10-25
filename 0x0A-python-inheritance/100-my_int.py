#!/usr/bin/python3
class MyInt(int):
    """ class inherits from class int """

    def __eq__(self, other):
        """ method returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ method returns == check """
        return int.__eq__(self, other)
