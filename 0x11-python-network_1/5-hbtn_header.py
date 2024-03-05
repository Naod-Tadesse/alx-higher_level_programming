#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
from sys import argv
import requests

if __name__ == "__main__":
    resp = requests.get(argv[1]).headers
    print(resp.get("X-Request-Id"))
