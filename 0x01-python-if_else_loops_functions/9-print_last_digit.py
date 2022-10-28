#!/usr/bin/python3
"""Function that prints the last digit in singly linked list"""


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
