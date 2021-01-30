# /usr/bin/env python3.8
# coding:utf-8

"""
@file: object_init.py
@time: 2021/1/26 8:41 下午
@author:XF
"""


# 全局方法
def sleep(name):
    return name


class Person(object):

    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} 在奔跑')

    def jump(self):
        print(f'{self.name} 在跳跃')

    def work(self):
        self.run()
        self.jump()
        result = sleep(self.name)  # 可以调用全局方法
        print('sleep result is ', result)


xiaomu = Person(name='夏目', age=10)
xiaomu.name = 'xiaomu'
xiaomu.jump()

dewei = Person('dewei')
dewei.jump()
dewei.top = 174  # 添加属性，不会改变原有的类的属性

print(dewei.top)
print(dewei.age)

print('---------------')
xiaomu.work()
