#!/usr/bin/python3
"""
This module contains an implementation for a list
"""


class MyList:
    """
    This class represent a list
    """

    def __init__(self):
        self.list = []

    @property
    def list(self):
        """The list property."""
        return self.__list

    @list.setter
    def list(self, value):
        self.__list = value

    def append(self, element):
        self.list.append(element)

    def print_sorted(self):
        print(sorted(self.list))

    def __str__(self):
        return str(self.list)
