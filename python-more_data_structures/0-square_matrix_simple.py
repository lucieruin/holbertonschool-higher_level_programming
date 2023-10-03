#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        square = []
        for num in row:
            square.append(num ** 2)
        result.append(square)
    return result
