#!/usr/bin/python3
def lookup(obj):
	"""This function returns a list of available
	   attributes and methods of an object
	args:
	    obj: instance of a class
	Returns:
		list of attributes
	"""
	return dir(obj)
