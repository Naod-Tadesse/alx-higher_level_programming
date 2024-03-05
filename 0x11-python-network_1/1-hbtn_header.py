#!/usr/bin/python3
"""request id"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    link = argv[1]

    with urllib.request.urlopen(link) as result:
        print(result.headers['X-Request-Id'])

