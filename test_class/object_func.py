# /usr/bin/env python3.8
# coding:utf-8

"""
@file: object_func.py
@time: 2021/2/1 9:18 下午
@author:XF
"""


class Test(object):
    def __str__(self):
        return 'this is a test class'

    def __getattr__(self, key):
        return '这个key:{}并不存在'.format(key)


t = Test()
print(t)
print(t.a)  # 用了getattr函数就会很友好的不会让程序报错
print(t.b)