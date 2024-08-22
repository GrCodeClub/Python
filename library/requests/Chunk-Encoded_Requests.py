# Εάν χρειάζεται να στείλεις δεδομένα σε κομμάτια, μπορείς να χρησιμοποιήσεις chunked transfer encoding:
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Δημιουργία Session με HTTPAdapter για chunked requests
session = requests.Session()
adapter = HTTPAdapter(max_retries=Retry(total=3, backoff_factor=0.1))
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.post('https://httpbin.org/post', data=iter(['chunk1', 'chunk2']))
