#!/usr/bin/python3
def is_same_class(obj, a_class):
	"""function returns True/false if obj is type of a class
	args:
	     obj: object
	     a_class: class type

	Returns:
		True if type of obj is a_class
		false,otherwise
	"""

	return type(obj) is a_class
