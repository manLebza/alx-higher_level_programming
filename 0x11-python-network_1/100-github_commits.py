#!/usr/bin/python3
"""
Module shows the last 10 commits of a repository in GitHub
"""
from requests import get, auth
from sys import argv

if __name__ == "__main__":
    try:
        rep = argv[1]
        owner = argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, rep)
        req = get(url)
        json_o = req.json()
        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'),
                  json_o[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
