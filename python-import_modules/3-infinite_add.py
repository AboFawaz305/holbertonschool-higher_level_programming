#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    converted_args = [int(arg) for arg in argv[1:]]
    print("{}".format(sum(converted_args)))
