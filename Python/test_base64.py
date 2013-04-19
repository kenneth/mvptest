#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
s = '我是字符串'
a = base64.b64encode(s)
print a
print base64.b64decode(a)
print base64.b64decode('R2VuZXJhbCBEaXNjdXNzaW9u')
print base64.b64decode('QWR2YW5jZWQgUGx1Z2luIFVzYWdl')
