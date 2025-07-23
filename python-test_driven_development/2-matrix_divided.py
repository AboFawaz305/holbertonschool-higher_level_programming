#!/usr/bin/python3
"""
This module contains function to perform division on a matrix
"""


def matrix_divided(matrix, div):
    """This function divides div on every element in matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for elem in row:
            if type(elem) is not float and type(elem) is not int:
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats"
                )
    rowSize = len(matrix[0])
    for row in matrix:
        if len(row) != rowSize:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
