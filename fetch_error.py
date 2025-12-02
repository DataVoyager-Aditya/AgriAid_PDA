import urllib.request
from urllib.error import HTTPError

try:
    response = urllib.request.urlopen('http://127.0.0.1:8080/about')
    print(response.read().decode('utf-8'))
except HTTPError as e:
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
