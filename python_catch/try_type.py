# /usr/bin/env python3.8
# coding:utf-8

"""
@file: try_type.py
@time: 2021/2/6 7:22 下午
@author:XF
"""


class test(object):
    pass


t = test()
try:
    t.name
except AttributeError as e:
    print(e)

d = {'name': '小慕'}
try:
    d['age']
except KeyError as e:
    print('没有对应的键', e)

l = [1, 2, 3]
try:
    l[5]
except IndexError as e:
    print(e)

name = 'dewei'
try:
    int(name)
except ValueError as e:
    print(e)


def test(a):
    return a


try:
    test()
except TypeError as e:
    print(e)
