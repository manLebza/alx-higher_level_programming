#!/usr/bin/python3
"""
this module is composed by a function that divides numbers of a matrix
"""

def matrix_divided(matrix, div):
    """function that divides integer/float numbers of a matrix
    args:
        matrix: list of a lists of integer/float numbers of a matrix
        div: number which devides the matrix

    Returns:
        A new matrix with the division ressults

    Raises:
        TypeError: if elements of the matrix are not lists
                   if elements of the lists aren't integers/floats
                   if div is not an integer/float number
                   if the lists of the matrix don't have the same size
        ZeroDivisionError: if div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division zero")
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_type = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
