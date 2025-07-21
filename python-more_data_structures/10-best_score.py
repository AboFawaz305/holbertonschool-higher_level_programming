#!/usr/bin/python3


def reduce(func, seq, acc):
    if len(seq) == 0:
        return acc
    return reduce(func, seq[:-1], func(seq[-1], acc))


def compare_key(key1, key2):
    if key1[1] > key2[1]:
        return key1
    return key2


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.items()) == 0:
        return "None"
    return reduce(compare_key, list(a_dictionary.items()), ("", -999))[0]


if __name__ == "__main__":
    a_dictionary = {"John": 12, "Bob": 14, "Mike": 14, "Molly": 16, "Adam": 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
