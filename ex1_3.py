import requests

url = "http://www.baidu.com/s"
kv = {'wd': 'Python'}
r = requests.get(url, params = kv)
print r.status_code
print r.request.url

url = "http://www.so.com/s"
kv = {'q': 'Python'}
r = requests.get(url, params = kv)
print r.status_code
print r.request.url
