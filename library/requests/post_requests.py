# Απλό POST αίτημα
import requests

url = 'https://grcodeclub.gr/post'
data = {'key': 'value'}
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())
