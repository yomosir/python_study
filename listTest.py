# -*- coding: utf-8 -*-
a = []
print type(a)
b = ['a',23,"asddasd"]
print b
print b[0]
"""
1.list的分割方法与字符串相同，还有index()方法
2.list还有一种倒序的标号，最右边第一个为-1，然后依次往左-2，-3...
"""
print b[-1]
"""
list反转
方法一：b[::-1]
方法二：list(reversed(b))->也可以对字符串操作
"""
print b[::-1]
print list(reversed(b))
print list(reversed("asdf"))
c = list(reversed("asdf"))
print type(c)
"""
对list相关的操作与字符串相同->拼接，重复（*），in（判断是否在其中），最大最小值（max(),min()），
比较cmp

对list追加元素
1.使用append()
2.先使用len()方法求出长度a，然后b[a:] = ["追加元素"]
注意：如果写成b[a:] = "追加元素"，则字符串中的每一个元素都会成为list中的一个元素
"""
b.append("123")
print b
d = len(b)
b[d:] = ["append"]
print b
"""
append->整体化追加 与 extend方法->个体化扩编
两个方法都是原地修改列表，既然是原地修改就没有返回值。而且追加的类型必须是iterable(可以迭代的类型)
如果是字符串变会一个一个字符的拆开
"""
lis = [1,2,3]
li = [1,2]
lis.append(li);
print lis
lis.extend(li);
print lis
"""
count()方法数一数一个元素在该list中出现多少次，insert(index,elem)
remove(x)删除list中出现的第一个x，如果没有x就会出错
pop(i)删除第i个元素，并返回删除的元素值，如果没有标明i，则会删除并返回最后一个元素
reverse()倒序
sort()默认从小到大排序，sort(reverse=True)，从大到小排序,还有一个参数key，当key = len就会按照长度来排序
"""
lis = [1,2,3]
lis.insert(0,22)
print lis
lis.remove(22)
print lis
print lis.pop(0)
print lis.pop()
lst = ["python","java","c","pascal"]
lst.sort(key = len)
print lst
#字符串和列表的区别：
"""
列表是可以改变的，而字符串是不可以改变的。列表的许多方法可以对列表进行原地修改，而字符串不可以
"""
#元组
t = 1,2,3,[1,2]
print t
print type(t)
#切片与list相同
"""
list 和 tuple可以相互转化,分别使用的是list()和tuple()方法
"""
ls = [1,2,3]
tup = 1,2,3,4
tls = tuple(ls)
print tls
ltup = list(tup)
print ltup



