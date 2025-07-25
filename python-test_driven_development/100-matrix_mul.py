#!/usr/bin/python3
"""
This module contains function for mtrix multipication
"""


def dot_product(v1, v2):
    """
    Returns the dot product of v1 and v2
    """
    return sum([x * y for x, y in zip(v1, v2)])


def matrix_mul(m_a, m_b):
    """
    Returns the result of multiplying
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for r in m_a:
        if type(r) is not list:
            raise TypeError("m_a must be a list of lists")
        for e in r:
            if type(e) is not int and type(e) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for r in m_b:
        if type(r) is not list:
            raise TypeError("m_b must be a list of lists")
        for e in r:
            if type(e) is not int and type(e) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    a_rows_size = len(m_a[0])
    for r in m_a[1:]:
        if len(r) != a_rows_size:
            raise TypeError("each row of m_a must be of the same size")
    b_rows_size = len(m_b[0])
    for r in m_b[1:]:
        if len(r) != b_rows_size:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[dot_product(row, col) for col in zip(*m_b)] for row in m_a]
