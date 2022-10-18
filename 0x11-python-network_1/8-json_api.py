#!/usr/bin/python3
'''
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
'''
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'value': q})
    try:
        j = r.json()
        if j == {}:
            print('No result')
        else:
            print("[{}] {}".format(j.get('id'), j.get('name')))
    except ValueError:
        print('Not a valid JSON')
