# Αίτημα με αυθεντικοποίηση
import requests
from requests.auth import HTTPBasicAuth

url = 'https://grcodeclub.gr/basic-auth/user/pass'
response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
print(response.status_code)
print(response.json())
