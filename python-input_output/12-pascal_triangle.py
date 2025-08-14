#!/usr/bin/python3
"""
Functions to get a pascal triangle
"""


def fact(n):
    """
    Returns the factorial of n
    """
    if n <= 1:
        return 1
    return n * fact(n - 1)


def choose(n, k):
    """
    Returns n choose k
    """
    return fact(n) // (fact(k) * fact(n - k))


def pascal_triangle(n):
    """
    Returns pascal triangle of length n
    """
    return [[choose(r, k) for k in range(r + 1)] for r in range(n)]
