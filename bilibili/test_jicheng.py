# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_jicheng.py
@time: 2021/2/23 11:05 上午
@author:XF
"""
'''
测试继承的基本使用
'''


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print('年龄，年龄我也不知道')


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显示的调用父类初始化方法，不然解释器不回去调用
        self.score = score


# Student------>Person------>object
print(Student.mro())

s = Student('徐飞', 18, 100)
s.say_age()

print(s.name)                               

