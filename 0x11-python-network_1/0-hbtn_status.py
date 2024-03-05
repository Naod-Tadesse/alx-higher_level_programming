#!/usr/bin/python3

import urllib.request

link = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(link) as result:
    resp = result.read()
    print("Body response:")
    print(f"	- type: {type(resp)}")
    print(f"	- content: {resp}")
    print(f"	- utf8 content: {resp.decode('utf-8')}")
