#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld > 5:
    print(f"Last digit of {number: d} is {ld} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {number: d} is {ld} and is 0")
elif ld < 6 & ld != 0:
    print(f"Last digit of {number: d} is {ld} and is less than 6 and not 0")