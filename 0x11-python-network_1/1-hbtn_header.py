#!/usr/bin/python3
""" Module takes in a URL,Sends a request and displays the value
of the X-Request-Id variable found in the header.
"""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = Request(url)
    with urlopen(request) as response:
        html = response.info()
        print(dict(response.headers).get("X-Request-Id"))
