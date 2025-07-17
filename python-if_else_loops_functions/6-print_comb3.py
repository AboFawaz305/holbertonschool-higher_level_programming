#!/usr/bin/python3
for i in [x for x in range(0, 89) if x / 10 < x % 10]:
    print("{:0>2}".format(i), end=", ")
print("{:0>2}".format(89))
