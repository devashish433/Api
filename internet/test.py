from urllib import response
import requests


result = requests.get('http://127.0.0.1:5000/app/api/data')
print(result.status_code)
print(result.json())