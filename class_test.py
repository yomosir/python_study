# -*- coding: utf-8 -*-
"""this file is for the study of class"""
"""
类的创建
_init_函数是一个初始化函数，其中self就是一个类本身实例，就相当于类本身。有点类似于java中的this
"""
#first way
_metaclass_ = type
class Person:
    def _init(self,name):
        self.name = name
#second way
class cc(object):
    x = 10
#example:P类的x是类属性，foo.x是实例属性，这两个是不一样
#结论：类属性不受实例属性影响，实例属性会受类属性影响
class P(object):
    x = 7
print P.x
foo = P();
print foo.x
foo.x += 1
print foo.x
print P.x
#当类中变量引用的是可变对象（如list）时。类属性和实例属性都能直接修改
class B(object):
    y = [1,2,3]
bar = B()
print bar.y
bar.y.append(4)
print bar.y
print B.y
# Namespace
"""
命名空间因为对象的不同分为三种：
    内置命名空间：Built-in namespaces
    全局命名空间：Module:Global namespaces
    本地命名空间：Function&Class: Local namespaces
丛里到外的顺序：Local namespaces -> Global namespaces -> Built-in namespaces
"""
def fooo(num,str):
    name = "qiwsir"
    print locals()
fooo(221,"qiwsir")
#继承