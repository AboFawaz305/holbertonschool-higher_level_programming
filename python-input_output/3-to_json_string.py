#!/usr/bin/python3
"""
Functions to jsonify an object
"""
import json


def to_json_string(my_obj):
    """
    jsonify my_obj
    """
    return json.dumps(my_obj)
