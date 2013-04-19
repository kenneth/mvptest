#!/usr/bin/env python
#! coding: utf-8
import simplejson

d= {'apple': 'cat', 'banana':'dog', 'pear':'fish'}
print type(d)

x= simplejson.dumps(d)

print x
print type(x)

data=simplejson.loads(x)
print data
print type(data)
