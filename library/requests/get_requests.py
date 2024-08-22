import requests

response = requests.get('https://grcodeclub.gr')
print(response.status_code)
print(response.json())
