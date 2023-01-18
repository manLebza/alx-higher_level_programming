#!/usr/bin/python3
"""
Module fetches a URL with requests package
"""
import requests

if __name__ == "__main__":
    r = request.get('https://intranet.hbtn.io/status')
    t = r.text
    print('Body response: \n\t- type: {}\n\t- content: {}'.format(type(t), t))
