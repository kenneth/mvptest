#!/usr/bin/env python
#! coding: utf-8
import base64
import StringIO

a = "this is a test"
b = base64.encodestring(a) # 对字符串编码
print b
print base64.decodestring(b) # 对字符串解码

c = StringIO.StringIO()
c.write(a)
d = StringIO.StringIO()
e = StringIO.StringIO()
c.seek(0)
base64.encode(c, d) # 对StringIO内的数据进行编码
print d.getvalue()
d.seek(0)
base64.decode(d, e) # 对StringIO内的数据进行解码
print e.getvalue()

a = "this is a +test"
b = base64.urlsafe_b64encode(a) # 进行url的字符串编码
print b
print base64.urlsafe_b64decode(b)
