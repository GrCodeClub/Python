# Αίτημα με προσαρμοσμένα headers

import requests

url = 'https://grcodeclub.gr/headers'
headers = {'User-Agent': 'my-app'}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
