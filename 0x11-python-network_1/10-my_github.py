#!/usr/bin/python3
"""
This script takes GitHub credentials (username and password) and uses the GitHub API to display the user's id.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)

