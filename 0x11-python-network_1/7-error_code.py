#!/usr/bin/python3
"""
Module sends a request to the URL and displays:
    - The body of the response if there are no errors
    - The error code when there is an http error.
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    req = get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
