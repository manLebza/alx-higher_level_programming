#!/usr/bin/python3
"""
Module sends a POST requset to the URL and to
a URL with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except:
        pass

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = r.json()
        if not json_o:
            print("No Results")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except:
        print("Not a valid JSON")
