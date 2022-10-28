#!/usr/bin/python3
"""Module remove charactor in string."""


def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
