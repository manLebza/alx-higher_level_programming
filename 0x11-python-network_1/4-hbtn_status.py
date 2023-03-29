#!/usr/bin/python3
"""
Module fetches a URL with requests package
"""
from requests import get

if __name__ == "__main__":
    r = get('https://intranet.hbtn.io/status')
    rt = r.text
    print('Body response: \n\t- type: {}\n\t- content: {}'.format(type(rt),
          rt))
