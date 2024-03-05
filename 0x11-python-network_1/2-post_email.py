#!/usr/bin/python3
"""this sends request with email param"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    re = urllib.request.Request(url, data)

    with urllib.request.urlopen(re) as resp:
        result = resp.read()
        print(result.decode("utf-8"))
