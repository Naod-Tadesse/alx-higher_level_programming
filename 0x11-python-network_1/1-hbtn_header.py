#!/usr/bin/python3
"""request id"""

import urllib.request
import sys

if __name__ == "__main__":
    link = sys.argv[1]

    with urllib.request.urlopen(link) as result:
        print(result.headers['X-Request-Id'])

