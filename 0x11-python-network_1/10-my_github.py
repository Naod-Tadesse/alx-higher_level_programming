#!/usr/bin/python3
"""authenticate to github api"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    github_api = "https://api.github.com/user"
    result = requests.get(github_api, auth=(argv[1], argv[2]))
    print(result.json().get("id"))
