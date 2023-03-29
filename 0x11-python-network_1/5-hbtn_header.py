#!/usr/bin/python3
"""
Module snds a request to the URL and displays
the value of a variable in the response header.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    try:
        r = get(argv[1])
        print(r.headers.get(['X-Request-Id']))
    except IndexError:
        pass
