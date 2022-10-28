#!/usr/bin/python3
"""In this module we implement a magic calculator"""


def magic_calculation(a, b, c):
    """Match byte code provided by Holberton School"""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a * b - c)
