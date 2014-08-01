#!/usr/bin/python

import requests

# set login parameters and url

payload = {'auth_pass': 'cartel'}

url = 'http://192.168.3.1:8000/?redirurl=http%3A%2F%2Fgoogle.com%2F'

r = requests.get(url, params=payload)

print(r, url)

