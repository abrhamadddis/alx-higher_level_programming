#!/usr/bin/python3
'''
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''

import requests
import sys

if __name__ == "__main__":
    usrname = sys.argv[1]
    url = f"https://api.github.com/users/{sys.argv[1]}"
    res = requests.get(url,  auth=requests.auth.
                       HTTPBasicAuth('{sys.argv[1]}', '{sys.argv[2]}'))
    if res.status_code >= 400:
        print('None')
    else:
        print(res.json().get('id'))
