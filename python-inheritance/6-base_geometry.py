#!/usr/bin/python3
"""
This module cotains classes to represent geometry
"""


class BaseGeometry:
    """This class represent geometry"""

    def area(self):
        raise Exception("area() is not implemented")
