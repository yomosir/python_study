# -*- coding: utf-8 -*-
"""
this file is for the study of operating of file
"""
"""
open file and print the content of a file
"""
"""
使用open函数读取文件，用for循环来输出内容，注：如果不写line后面的逗号，就会换两次行，加上
逗号，就只会换一次行！
"""
f = open("test.txt")
for line in f:
    print line,

for line2 in f:
    print line2,
"""
创建文件
r:以读的方式打开文件
w:以写的方式打开文件
a:以追加的方式打开
打开文件后一定要close()
"""
nf = open("121.txt","w")
nf.write("this is new file")
"""
使用with
"""
with open("test.txt","r") as f:
    print  f.read()
"""
文件的状态
"""
import os
file_stat = os.stat("test.txt")
print file_stat
print file_stat.st_ctime
import time
print time.localtime(file_stat.st_ctime)



