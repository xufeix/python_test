# /usr/bin/env python3.8
# coding:utf-8

"""
@file: object_parent_chlid.py
@time: 2021/1/29 5:31 下午
@author:XF
"""

#git 练习

class Parent(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def talk(self):
        return f'{self.name} are walking'

    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is a boy'
        else:
            return f'{self.name} is a girl'


class ChildOne(Parent):
    def paly_football(self):
        return f'{self.name} are palying football'


class ChildTwo(Parent):
    def paly_pingpong(self):
        return f'{self.name} are playing pingpong'


c_one = ChildOne('小慕', '女')
result = c_one.paly_football()
print(result)
result = c_one.talk()
print(result)

c_two = ChildTwo('小慕叭叭', '男')
result = c_two.paly_pingpong()
print(result)
result = c_two.talk()
print(result)


p = Parent(name='小慕爸爸', sex='boy')
result = p.talk()
print(result)
result = p.is_sex()
print(result)