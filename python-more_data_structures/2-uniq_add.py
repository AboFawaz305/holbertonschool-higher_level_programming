#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = sorted(my_list)
    uniq_list = [i
                 for p, i in enumerate(sorted_list)
                 if i not in sorted_list[p + 1:]]
    return sum(uniq_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
