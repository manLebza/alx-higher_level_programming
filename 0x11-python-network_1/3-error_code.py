#!/usr/bin/python3
"""
Module takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
handling HTTP errors.
"""

from urllib import request, errors
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
