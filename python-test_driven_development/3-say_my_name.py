#!/usr/bin/python3
"""
This module contains function to print names
"""


def say_my_name(first_name, last_name=""):
    """print a name in the format: My name is <first name> <last name>"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
