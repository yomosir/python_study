# -*- coding: utf-8 -*-
"""
算术运算符：+,-,*,/,%,**(次方),//(去尾法取商的整数部分)
"""
"""
比较运算符：==,!=,>,<,>=,<=
"""
"""
bool运算：and , or , not() 
"""
print 4 > 3 and 3 < 5
print 4 > 5 or 3 > 1
print not(3 > 2)
"""
simple sentence:
1.print
print 默认后面是有一个\n换行的，但当使用","时，就不会换行了，在循环时候会用到
"""
print "Hello,world"
print "Hello","world"
"""
import :引入模块
1.import math:math.pow()
2.from math import pow:这样就可以直接使用pow()方法
3.from math import pow as pinfang:pinfang() = pow()
4.from math import pow,e,pi:引入多个
"""
"""
赋值:=
"""
x,y,z = 1,2,3
print x
print y
print z
x,y=y,x
print x
print y
"""
条件语句:
if 条件:
    语句块1(前面有4个空格)
elif 条件:
    语句块2
    ...
else:
    语句块3
"""
#print "please input a number:"
x = int(raw_input("please input a number:"))
if x == 10:
    print "hello" 
elif x > 10:
    print "sb"
elif x < 10:
    print "world"
else:
    print "error"
"""
三元操作符
A = Y if X else Z
如果X为真，则执行A = Y
如果X为假，则执行A = Z
"""
x = 3 if True else 4
print x
"""
for 循环基本结构
    for 循环规则:
        操作语句
"""
hello = "world"
for i in hello:
    print i

for i in range(len(hello)):
    print hello[i]
lis = ["hello","world","welcome"]
print lis
for word in lis:
    print word
"""
range(start,stop[,step])方法
this function can create a list containing number elements;
这个函数最长应用与for循环
函数参数必须是整数，默认从0开始，返回值是类似[start,start+step,start + 2 * step,...]的列表
step默认值是1，
如果step是正数，返回list的最后的值不包含stop值，start + istep < stop
step是负数，start + istep > stop
step不等于0
参数：
start：开始数值，默认为0
stop：结束数值，必须写
step：变化步长，默认是1
"""
print range(9)
print range(0,9)
print range(0,9,1)
print range(0,-9,-1)
"""
找出100以内能被3整除的正整数
"""
li = []
for i in range(1,100):
    if i % 3 == 0:
        li.append(i)

print li
"""
所有的序列类型对象都能够用for来循环
str,set,list,dictionary
"""
"""
函数zip()
zip()是内置函数，参数必须是某种序列类型数据，如果是字典，那么视为序列，让后将序列对应的元素一次组成元素，并单做列表中的元素
"""
a = [1,2,3,4]
b = [5,6,7,8]
print zip(a,b)
c = "asdas"
print zip(c)
d = []
for x,y in zip(a,b):
    d.append(x + y)
print d
"""
enumrate()
返回一个枚举的对象，必须是序列，可以迭代的数据
"""
seasons = ["Spring","Summer","Fall","Winter"]
print list(enumerate(seasons))
raw = "Do you love Cang? Cang is a good teacher."
print list(enumerate(raw))
rawl = raw.split(" ")
print list(enumerate(rawl))
"""
列表解析：
"""
power = [x**2 for x in range(1,10)]
print power
mybag = [' bag',' apple','green leaf ']
print [one.strip() for one in mybag]
"""
while 循环
while 条件:
      执行语句
"""
xxx = 2
while xxx > 3:
    print xxx
"""
for ... else: ...
跳出循环后要做的事情
"""
