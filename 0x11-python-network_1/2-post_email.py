#!/usr/bin/python3
"""
Python module takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response.
"""
from urllib.request import Request, urlopen
from urllib import parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
