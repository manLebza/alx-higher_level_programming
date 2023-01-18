#!/usr/bin/python3
"""
Module sends a search request to the Star Wars APi,
searching people.
"""
import requests
import sys

if __name__ == "__main__":
    page = 1
    while page:
        s = sys.argv[1]
        url = 'https://swapi.co/api/people/?search={}&page= {}'.fromat(s, page)
        r = requests.get(url)
        json_o = r.json()
        if page == 1:
            print("Number of results: {}".format(json_o.get('count')))
        for charactor in json_o.get('results'):
            print(charactor.get('name'))
        if not json_o.get('next'):
            break
        page = page + 1
