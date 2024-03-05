#!/usr/bin/python3
""" search for user using q as param"""
from sys import argv
import requests


if __name__ == "__main__":
    link = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        dat = {"q": ""}
    else:
        data = {"q": argv[1]}

    result = requests.post(link, data=dat)
    try:
        resp = result.json()
        if not (res == {}):
            print(f'[{resp.get("id")}] {resp.get("name")}')
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
