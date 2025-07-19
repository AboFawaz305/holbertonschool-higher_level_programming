#!/usr/bin/python3
for char_code in range(ord("z"), ord("a") - 1, -1):
    print(
        "{}".format(chr(char_code).upper()
                    if char_code % 2 == 1 else chr(char_code)),
        end="",
    )
