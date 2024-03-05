#!/usr/bin/python3
""" show error code if greater thatn 400"""
from sys import argv
import requests

if __name__ == "__main__":

    resp = requests.get(argv[1])
    if not (r.status_code >= 400):
        print(resp.text)
    else:
        print(f"Error code: {resp.status_code}")
