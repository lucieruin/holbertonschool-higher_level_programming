#!/usr/bin/python3
""" divides all elements of a matrix """


def matrix_divided(matrix, div):

    """ args:
            matrix : matrix of int or float
            div : divides matrix by int or float

        raises:
            TypeError: if [a] or [b] is not an int or a float
            TypeError: if row of matrix is not the same
            TypeError: if div is not an int or a float
            TypeError: if matrix is a list empty or not a list

            ZeroDivisionError: if div == 0

        Return: new matrix
    """

    errorMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(errorMsg)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(errorMsg)
        for col in matrix[0]:
            if type(col) is not int and type(col) is not float:
                raise TypeError(errorMsg)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            new[row][col] = round(matrix[row][col] / div, 2)

    return new
