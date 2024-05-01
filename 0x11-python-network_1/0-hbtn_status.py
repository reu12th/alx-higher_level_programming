#!/usr/bin/python3
"""
Python script Fetches https://intranet.hbtn.io/status
Use the package urllib
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
    as respon:
        html = respon.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
