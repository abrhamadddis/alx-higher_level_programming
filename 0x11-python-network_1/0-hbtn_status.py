#!/usr/bin/python3
"""
    it's python script  that fetches from https://alx-intranet.hbtnn.io.status
"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as file:
        html = file.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format((html)))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
