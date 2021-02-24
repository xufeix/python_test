# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_duotai.py
@time: 2021/2/24 3:14 下午
@author:XF
"""
'''
学习多态
bilibili  第109集
'''


class Man:
    def eat(self):
        print('饿了，吃饭了！')


class Chinese(Man):
    def eat(self):
        print('中国人用筷子吃饭')


class English(Man):
    def eat(self):
        print('英国人用叉子吃饭')


class Indian(Man):
    def eat(self):
        print('印度人用右手吃饭')


def manEat(m):
    if isinstance(m, Man):
        m.eat()  # 多态，一个方法调用，根据对象不同调用不同的方法
    else:
        print('不能吃饭')


manEat(Chinese())
manEat(English())
