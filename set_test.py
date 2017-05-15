#code: utf-8
"""
this file is to learn this type set
the element in the set can not be repeated
"""
#Create set
s1 = set("zgcggsscc")
print s1
s2 = set([123,"asd","face"])
print s2
s3 = {"facebook","sofa","bed"}#it is not advocating
print s3
"""
function:
add():add a element to a set
update():conbine the element from other set
"""
s1 = set(["a","b"])
s2 = set(["c","a"])
s1.add("e")
print s1
s1.update(s2)
print s1
"""
pop(): remove and return the first element from a set
remove() :remove a element from a set ,it must be a member.
discard():remove a element from a set if it is a member,if it
is not a member ,do nothing
clear():remove all elements from this set
"""
#set() 是一种可以原地修改的set，或者说是可以改变，也就是unhashable
#there is a hashable set，and can not be updated
"""
frozenset()
"""
f_set = frozenset("zgccc")
print f_set

"""
the operation of set:
1.元素和集合的关系：元素和集合就两种关系，一种是属于，还有一种是不属于
2.集合和集合的关系
    A和B是不是完全相等: == , !=
    A是否是B的子集:A < B 返回True则A是B的子集，也可以用A.issubset(B)判断
    A和B并集:a.union(b)
    A和B的交集:a & b,a.intersection(b)
    A相对B的差，即A相对B不同的部分元素:a.difference(b)
    A,B的对称差集：a.symmetic_difference(b)
"""

