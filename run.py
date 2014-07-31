import requests

passing = {'auth_pass': 'cartel'}
url = 'http://cartelcoffeelab.com'

r = requests.get(url, params=passing)


