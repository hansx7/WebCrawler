# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "error while linking"

def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
	template = "{0:{3}^10}{1:{3}^10}{2:{3}^10}"
	with open("中国最好大学排名.txt", "w") as f:
		f.write(template.format("排名", "学校", "总分", chr(12288)))
		f.write("\n")
		for i in range(num):
			u = ulist[i]
			f.write(template.format(u[0], u[1], u[2], chr(12288)))
			f.write("\n")

uinfo = []
url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
html = getHTMLText(url)
fillUnivList(uinfo, html)
printUnivList(uinfo, 20)