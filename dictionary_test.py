# -*- coding: utf-8 -*-
"""
This file is for the type which named dictionary，it is a type using KEY-VALUE
model to store data
"""
# Create a dictionary
mydic = {} #a empty dictionary
print mydic
person = {"name":"zgc","age":20}
print person

name = (["first","Google"],["second","Yahoo"])
webSite = dict(name)
print webSite

ad = dict(name = "zgc",age = 20)
print ad

website = {}.fromkeys(("third","forth"),"facebook")
print website
#the key is unique,but the the value is not unique，every KEY-VALUE use "," to separate
#add KEY-VALUE
person["stuid"] = 140522116
print person
#visit the value
print person['name']
"""
operation
len(): return the quantity of dictionary
del d[key]:delete the KEY-VALUE whose key is "key" in the dictionary which named d
"""
print len(person)
del person["name"]
print name
print "name" in person #the operation in is to judge the key whether KEY-VALUE is in the dictionary
city_code = {"suzhou":"0512"}
print "Suzhou is a beautiful city , its area code is %(suzhou)s" %city_code

"""
dictionary's function
"""
"""
copy() and deepcopy()
用"="使得两个变量相等，只是换一个代号，本质没有改变
copy():是浅拷贝，如果字典内有list类型的value值，那浅拷贝后内部list值拷贝前后是共享的
deepcopy():是深拷贝，能解决上面的问题
"""
import copy
a = {"name":"python","lang":["asd","df"]}
b = a
c = a.copy()
d = copy.deepcopy(a)
print id(a["lang"])
print id(b["lang"])
print id(c["lang"])
print id(d["lang"])
print id(a)
print id(b)
print id(c)
print id(d)
"""
clear():clear all the element of a dictionary
get():get the value by key
tips:while the key is not found in the dictionary,the way dic['key'] will return a error,but get() will return None
and there is a special example below:
"""
testa = {"lang":"zgc"}
newT = testa.get("name","python")
print newT
print testa
"""
setdefault():can add a KEY-VALUE to dic and get the value
"""
e = {"lang":"zgc"}
print e.setdefault("lang")
print e.setdefault("name","zgc")
print e
print e.setdefault("web")
print e
"""
items/iteritems keys/iterkeys values/itervalues
iteritems is an iterator 
"""
dd = {"name":"zgc","lang":"python","web":"www.gihub.com"}
dd_kv = dd.items()
print dd_kv
"""
pop(),update(),has_key():判断字典中是否存在某个key
"""



