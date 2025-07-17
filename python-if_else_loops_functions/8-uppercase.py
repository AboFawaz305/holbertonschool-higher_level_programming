#!/usr/bin/python3
def to_upper(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return chr(ord(c) - 32)
    return c


def uppercase(str):
    print("{}".format("".join([to_upper(c) for c in str])))
