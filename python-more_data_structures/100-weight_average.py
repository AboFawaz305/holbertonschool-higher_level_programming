#!/usr/bin/python3
def reduce(func, seq, acc):
    if len(seq) == 0:
        return acc
    return reduce(func, seq[:-1], func(seq[-1], acc))


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = reduce(lambda e, a: e[1] + a, my_list, 0)
    weighted_sum = reduce(lambda e, a: e[0] * e[1] + a, my_list, 0)
    return weighted_sum / weight
