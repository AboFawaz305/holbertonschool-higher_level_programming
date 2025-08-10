#!/usr/bin/python3
"""
Functions to save objects in files
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save my_obj in a file
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
