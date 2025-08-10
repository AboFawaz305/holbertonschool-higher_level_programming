#!/usr/bin/python3
"""
Reading data from a csv file
"""

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, mode="r", newline="") as f:
            csv_dict = [dict(r) for r in csv.DictReader(f)]
        with open("data.json", mode="w") as f:
            json.dump(csv_dict, f)
        return True
    except Exception as e:
        return False
