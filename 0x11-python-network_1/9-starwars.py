#!/usr/bin/python3
"""
Module sends a search request to the Star wars APi,
and searches people.
"""

import requests
import sys

if __name__ == "__main__":
    search = 'https://swapi.co/api/people/?search= {}'.format(sys.argv[1])
    r = requests.get(search)
    json_o = r.json()
    print("Number of results: {}".format(json_o.get('count')))
    for charactor in json_o.get('results'):
        print(charactor.get('name'))
