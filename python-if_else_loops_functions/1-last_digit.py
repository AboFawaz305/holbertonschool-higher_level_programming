#!/usr/bin/python3
import random
from math import log10, trunc

number = random.randint(-10000, 10000)
last_digit = 0
if number != 0:
    last_digit = int((abs(number) % 10) * number / abs(number))

print(f"Last digit of {number} is {last_digit} ", end="")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
