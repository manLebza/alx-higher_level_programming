#!/usr/bin/python3
"""Prints the numbers from 1 to 100 separated by a space,
    for multiples of three, print Fizz,
    for multiples of five, print Buzz,
    for multiples of three and five, print FizzBuzz instead of numbers
"""


def fizzBuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        elif number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(number), end="")
