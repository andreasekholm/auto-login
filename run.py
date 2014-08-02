#!/usr/bin/python

import requests
 
url = 'http://192.168.3.1:8000/?redirurl=http%3A%2F%2Fwww.google.com'
data = {
        'auth_user': 'cartel',
        'auth_pass': 'cartel',
        'redirurl': 'http://www.google.com',
        'accept': 'Continue'
}
 
r = requests.post(url, data=data)
print r.status_code

#@retry(wait_fixed=0)

