#!/usr/bin/python3
"""
function that divides all elements of a matrix.
Args: matrix(list of lists of integers or floats), div(integer or float)
Return: a new matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float or i is None:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) is not int and type(div) is not float or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return new_matrix
