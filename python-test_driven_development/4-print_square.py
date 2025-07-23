#!/usr/bin/python3
"""
This module contains function to print shapes
"""


def print_square(size):
    """Print a square of size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
