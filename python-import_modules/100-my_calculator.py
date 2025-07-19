#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit

    from calculator_1 import add, div, mul, sub

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    supported_operators = {"+": add, "-": sub, "*": mul, "/": div}
    args = [int(argv[1]), int(argv[3])]
    if argv[2] not in supported_operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    operator = supported_operators[argv[2]]
    print(f"{args[0]} {argv[2]} {args[1]} = {operator(args[0], args[1])}")
