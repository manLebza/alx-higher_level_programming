#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared2 = []

    for i in range(len(matrix)):
        squared = []

        for j in range(len(matrix[i])):
            squared.append(matrix[i][j] **2)

        squared2.append(squared)

    return (squared2)

