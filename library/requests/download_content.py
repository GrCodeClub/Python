import requests

url = 'https://www.grcodeclub.gr/somefile.zip'
response = requests.get(url)
with open('somefile.zip', 'wb') as file:
    file.write(response.content)
