#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit

    print("{} argument".format(len(argv) - 1), end="")
    if len(argv) <= 1:
        print("s.")
        exit()
    elif len(argv) == 2:
        print(":")
    else:
        print("s:")
    for pos, arg in enumerate(argv[1:]):
        print("{}: {}".format(pos + 1, arg))
