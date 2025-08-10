#!/usr/bin/python3
"""
A module containing a function that reads a file and print its content to
stdout"""


def read_file(filename=""):
    """
    Read the file and print its content
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        print(f.read(), end="")
