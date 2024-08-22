import requests

try:
    response = requests.get('https://api.github.com/invalid-url')
    response.raise_for_status()  # Θα προκαλέσει εξαίρεση για HTTP σφάλματα
except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')
    print(response.json())
