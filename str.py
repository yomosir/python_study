# -*- coding: utf-8 -*-
a = 1989
b = "free"
print b + `a`
print b + str(a) #str()是内置的函数，类似与toString()
print b + repr(a) #repr()函数是``反引号的替代品
dos = "c:\news"
print dos
dos = r"c:\news"
print dos #以r开头的字符串表示里面所有的字符串均为源氏字符串，没有转义
#print raw_input("input your name:")
print "I like %s" % "python"# The first way to format 
print "I like {}".format("python")
print "I like {0} and I like {1}".format("python","java")
print "I like {lang01} and I like {lang02}".format(lang01="python",lang02="java")#Use string.format() function to format
lang = "python"
print "I like %(program)s" %{"program":lang}#The last way to format
#解决中文乱码问题
#使用coding：utf-8
#在遇到字符串，立刻转化为unicode，不要用str()，直接用unicode()  ：
unicode_str = unicode('中文',encoding='utf-8')
print unicode_str.encode('utf-8')
#在对文件操作时，打开文件是最好用codecs.open代替open
#import codecs
#codece.open('filename',encoding='utf-8')
"""
字符串的分割
内置函数由split(),strip()<去掉字符串两边的空格>,len():返回字符串长度,cmp()比较两个子哦符传的序列值是否相同，即ASCII码大小(ord()输出ASCII码，chr()输出ASCII码所对应的字符)
"""
lang = "advantages"
print lang[0]
print lang[0:4]
print lang[:6]
print lang[3:]
"""
index()可以用来表示字符在字符串中的位置，如果是有重复的显示该字符在字符串中
第一次出现的位置
"""
print lang.index("a")
