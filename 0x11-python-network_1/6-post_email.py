#!/usr/bin/python3
"""
Module takes in a URL and an email address, tyhen sends
a POST request to the passed URL with the email, and
displays the body of the request.
"""

from requests import post
from sys import argv

if __name__ == "__main__":
    r = post(argv[1], data={'email': argv[2]})
    print(r.text)
