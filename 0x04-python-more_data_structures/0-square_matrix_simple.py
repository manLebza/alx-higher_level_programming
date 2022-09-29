#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = matrix(list(map(lambda x, y: x**2, squared)))

    for i in range(len(matrix)):
        new_matrix = [x**2 for i in matrix[i]]

    return (new_matrix)

