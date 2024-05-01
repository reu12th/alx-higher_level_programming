#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
The first argument will be the repository name
The second argument will be the owner name
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    m = requests.get(url)
    commits = m.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                commits[a].get("sha"),
                commits[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
