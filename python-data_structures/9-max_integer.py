#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_elem = my_list[0]
    for e in my_list[1:]:
        if e > max_elem:
            max_elem = e
    return max_elem
