#!/usr/bin/python3
"""
Module sends a POST requset to the URL and to
a URL with the letter as a parameter.
"""

from requests import post
from sys import argv

if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = argv[1]
    except IndexError:
        pass

    res = post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = res.json()
        if not json_o:
            print("No Results")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except TypeError:
        print("Not a valid JSON")
