# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_mro.py
@time: 2021/2/24 11:48 上午
@author:XF
"""
'''
测试mro()方法解析顺序
'''


class A:
    def aa(self):
        print('aa')

    def say(self):
        print('say AAA！')


class B:
    def bb(self):
        print('bb')

    def say(self):
        print('say BBB！')


class C(B, A):
    def cc(self):
        print('cc')


c = C()
print(C.mro())  # 打印层次结构
c.say()  # 解释器寻找方法'从左到右'的方式，此时会执行B类中的say

