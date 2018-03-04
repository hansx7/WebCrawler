import requests

url = "https://item.jd.com/5826236.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print r.text[:1000]
except Exception as e:
	print "error while linking"