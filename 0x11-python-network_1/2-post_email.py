#!/usr/bin/python3
'''a Python script that takes in a URL and an email,
sends a POST request to the passed  URL with the email
as a parameter, and displays the body of the response'''

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # print(email)
    data = {'email': email}
    edata = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, edata)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        print(data)
