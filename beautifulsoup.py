import requests
from bs4 import BeautifulSoup
import re

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print soup.prettify()

# tag = soup.a
# print soup.title
# print tag
# print tag.parent.name
# print tag.parent.parent.name

# print tag.attrs
# print tag.attrs['class']

# print type(tag.attrs)
# print type(tag)

# print tag.string
# print type(tag.string)

# # go down
# html = soup.html
# print html.contents
# print html.children
# print html.descendants

# # go up
# p = soup.p
# print p.parent
# print p.parents

# # go between siblings
# a = soup.a
# print a.next_sibling
# for i in a.next_siblings:
# 	print i
# print a.previous_sibling
# for i in a.previous_siblings:
# 	print i

for link in soup.find_all('a'):
	print(link.get('href'))

print(soup)
print(soup.find_all(string = re.compile("python")))