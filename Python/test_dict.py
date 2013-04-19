#!/usr/bin/env python
#! coding: utf-8
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
print dict
dict["w"] = "watermelon"
print dict
del(dict["a"])
print dict
#字典遍历
for k in dict:
    print "dict[%s] =" % k,dict[k]
#每个元素是一个key和value组成的元组，以列表的方式输出
print dict.items()
#调用items()实现字典的遍历
for (k, v) in dict.items():
    print "dict[%s] =" % k, v
#输出key的列表
print dict.keys()
#输出value的列表
print dict.values()
