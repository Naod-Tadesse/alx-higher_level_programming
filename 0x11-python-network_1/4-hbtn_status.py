#!/usr/bin/python3
"""sending get request using requests"""
import requests

if __name__ == "__main__":
    result = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"    - type: {type(result.text)}")
    print("    - content: {}".format(result.text))
