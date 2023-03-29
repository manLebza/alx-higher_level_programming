#!/usr/bin/python3
"""
Module takes GitHub credentials and uses the
GitHub APi to display the user id
"""
from requests.auth import HTTPBasicAuth
from requests import get
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth 
    user = argv[1]
    password = argv[2]
    res = get(url, auth=auth)
    print(res.json().get('id'))
