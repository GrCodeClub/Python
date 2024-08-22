import requests

params = {'param1': 'value1', 'param2': 'value2'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.status_code)
print(response.json())
