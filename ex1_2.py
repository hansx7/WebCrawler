import requests

url = 'https://www.amazon.com/'
r = requests.get(url)
print r.status_code
# r.encoding = r.apparent_encoding
# print r.status_code
# print r.text
# print r.request.headers

kv = {"user-agent": "Mozilla/5.0"}
r = requests.get(url, headers = kv)
print r.status_code