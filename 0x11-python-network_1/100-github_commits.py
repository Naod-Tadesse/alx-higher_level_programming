#!/usr/bin/python3
"""the 10 most recent commitx"""
from sys import argv
import requests


if __name__ == "__main__":
    repos = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    result = requests.get(url).json()
    try:
        for i in range(10):
            name = result[i].get("commit").get("author").get("name")
            print(f'{result.get("sha")}: {name}')
    except IndexError:
        pass
