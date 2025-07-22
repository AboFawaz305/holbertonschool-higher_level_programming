#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    j = 0
    while i < max(len(my_list_1), len(my_list_2)) and i < list_length:
        try:
            result.append(my_list_1[i] / my_list_2[j])
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            i += 1
            j += 1
    return result
