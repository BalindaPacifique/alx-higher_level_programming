#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest) of a given repository by the specified owner.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

