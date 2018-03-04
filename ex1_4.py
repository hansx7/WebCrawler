# -*- coding:utf-8 -*-

import requests
import os

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1519323882641&di=94458bdcbf3f5ebe1181056758c76a56&imgtype=0&src=http%3A%2F%2Fcimg2.163.com%2Flady%2F2007%2F8%2F10%2F200708101117327cc74.jpg"
path = "/home/shycg/图片/hermione.jpg"
try:
	r = requests.get(url)
	with open(path, 'wb') as f:
		f.write(r.content)
		f.close()
		print "file saved"
except Exception as e:
	raise e