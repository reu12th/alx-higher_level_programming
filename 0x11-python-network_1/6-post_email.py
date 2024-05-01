#!/usr/bin/python3
"""
Sends a POST request to URL with a given email.
Usage: ./6-post_email.py <URL> <email>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    request = requests.post(url, data=value)
    print(request.text)
