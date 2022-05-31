#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    z = number * -1
else:
    z = number
r = z % 10
if r > 5:
    print("Last digit of", number, "is", r, "and is greater than 5")
elif r == 0:
    print("Last digit of", number, "is", r, "and is 0")
else:
    print("Last digit of", number, "is", r, "and is less than 6 and not 0")
