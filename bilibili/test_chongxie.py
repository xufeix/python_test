# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_chongxie.py
@time: 2021/2/23 4:29 下午
@author:XF
"""


class Person():

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print('我的年龄', self.__age)

    def say_introduce(self):
        print('我的名字是{0}'.format(self.name))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显示的调用父类初始化方法，不然解释器不回去调用
        self.score = score

    def say_introduce(self):
        # 重写了父类的方法
        print('报告老师，我的名字是，{0}'.format(self.name))


# Student------>Person------>object

s = Student('徐飞', 18, 100)
s.say_age()
s.say_introduce()
