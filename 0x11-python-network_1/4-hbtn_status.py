#!/usr/bin/python3
"""
Module: 4-hbtn_status
Fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

