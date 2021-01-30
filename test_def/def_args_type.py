# /usr/bin/env python3.8
# coding:utf-8

"""
@file: def_args_type.py
@time: 2021/1/25 4:22 下午
@author:XF
"""


def add(a: int, b: int = 3):
    print(a + b)


add(1, 2)
add('hello', 'xiaomu')


def test(a: int, b: int = 3, *args: int, **kwargs: str):
    print(a, b, args, kwargs)


test(1, 2, 3, '4', name='小慕')


def test2(a: int, b, c=3):
    print(a, b, c)


test2(1, 3, 4)
