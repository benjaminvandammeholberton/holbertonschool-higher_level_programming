#!/usr/bin/python3
import random
number = random.randint(-10000, 0)
absolute_last_digit = abs(number) % 10
if number < 0:
    last_digit = - absolute_last_digit
else:
    last_digit = absolute_last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
if last_digit <= 5 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and \
is less than 6 and not 0")
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
