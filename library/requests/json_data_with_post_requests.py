# Αποστολή JSON δεδομένων με POST αίτημα
import requests
import json

url = 'https://httpbin.org/post'
headers = {'Content-Type': 'application/json'}
json_data = {'key': 'value'}
response = requests.post(url, headers=headers, data=json.dumps(json_data))
print(response.status_code)
print(response.json())
