#!/usr/bin/python3
""" headers from get request """
from sys import argv
import requests

if __name__ == "__main__":
    resp = requests.get(argv[1]).headers
    print(resp.get("X-Request-Id"))
