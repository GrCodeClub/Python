# GET αίτημα με παραμέτρους
import requests

params = {'param1': 'value1', 'param2': 'value2'}
response = requests.get('https://grcodeclub.gr/get', params=params)
print(response.status_code)
print(response.json())
