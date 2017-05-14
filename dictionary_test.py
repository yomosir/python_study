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
#the key is unique,but the the value is not unique，every KEY-VALUE use "," to separate
#add KEY-VALUE
person["stuid"] = 140522116
print person


