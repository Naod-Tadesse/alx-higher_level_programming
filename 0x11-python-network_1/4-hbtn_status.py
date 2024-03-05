#!/usr/bin/python3
"""Python script that fetches a url"""
import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:\n	- type: {type(res.text)}")
    print(f"	- content: {res.text}")
