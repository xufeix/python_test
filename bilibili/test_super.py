# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_super.py
@time: 2021/2/24 2:58 下午
@author:XF
"""
'''
测试super（），代表父类的定义，而不是父类的对象
bilibili  108上学堂python教程400集第108集
'''


class A:
    def say(self):
        print('A:', self)


class B(A):
    def say(self):
        A.say(self)
        super().say()
        print('B:', self)


B().say()