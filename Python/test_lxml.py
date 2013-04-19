#coding=utf-8

import urllib
from lxml import etree

html = urllib.urlopen('http://www.douban.com/').read()

page = etree.HTML(html.lower().decode('utf-8'))
hrefs = page.xpath(u"//a")

for href in hrefs:
	print href.attrib

for href in hrefs:
	print href.attrib['href']

title = page.xpath(u'//title/text()')
print title

item = page.xpath(u'//*[@id="bd"]/h1/text()')
print item