#!/usr/bin/python3

print("{}"
      .format("".join([chr(c) for c in range(ord("a"), ord("z") + 1)
                       if chr(c) != "q" and chr(c) != "e"])),
      end="")
