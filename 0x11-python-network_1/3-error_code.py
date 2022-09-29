#!/usr/bin/python3
'''a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).'''

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode('utf-8')
            print(res)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
