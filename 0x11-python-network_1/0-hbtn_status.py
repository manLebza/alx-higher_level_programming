#!/usr/bin/python3
""" Module fetches https://alx-intranet.hbtn.io/status """
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as res:
        html = res.read()
    print("Body response:")
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode("utf-8")))
