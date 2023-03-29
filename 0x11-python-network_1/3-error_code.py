#!/usr/bin/python3
"""
Module takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
handling HTTP errors.
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
