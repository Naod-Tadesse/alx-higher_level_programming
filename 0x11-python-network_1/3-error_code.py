#!/usr/bin/python3
"""this script shows error"""
import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            result = resp.read()
            print(result.decode('UTF-8'))
    except error.HTTPError as error:
        print(f"Error code: {error.code}")
