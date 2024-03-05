#!/usr/bin/python3
"""send post request with email"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    dat = urllib.request.Request(argv[1])
    with urllib.request.urlopen(dat) as resp:
        result = resp.headers
        print(dict(result).get("X-Request-Id"))
