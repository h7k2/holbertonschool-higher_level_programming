#!/usr/bin/python3

import random

number = random.randint(-10, 10)
print(number)

if number > 0:
    print("number is greater than 0")

elif number == 0:
    print("number is 0")

else:
    print("number is less than 0")
