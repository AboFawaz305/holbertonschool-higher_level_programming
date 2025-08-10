#!/usr/bin/python3
"""
append arguments to a json file
"""
import json
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

old_args = []
try:
    old_args = load_from_json_file("add_item.json")
except Exception:
    pass
new_args = old_args + sys.argv[1:]
save_to_json_file(new_args, "add_item.json")
