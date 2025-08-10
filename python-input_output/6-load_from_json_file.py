#!/usr/bin/python3
"""
Functions to load objects from files
"""
import json


def load_from_json_file(filename):
    """
    load an object from a file
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.load(f)
