#!/usr/bin/python3
"""send post request with email"""
from sys import argv
import requests

if __name__ == "__main__":
    resp = requests.post(argv[1], data=argv[2])
    print(resp.text)
