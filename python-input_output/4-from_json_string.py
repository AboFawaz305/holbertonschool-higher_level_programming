#!/usr/bin/python3
"""
Functions to return an object from a json string
"""
import json


def from_json_string(my_str):
    """
    transform my_str to an object
    """
    return json.loads(my_str)
