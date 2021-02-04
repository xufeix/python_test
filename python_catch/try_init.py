# /usr/bin/env python3.8
# coding:utf-8

"""
@file: try_init.py
@time: 2021/2/4 4:31 下午
@author:XF
"""


def upper(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()
    except Exception as e:
        print('程序出错了{}'.format(e))
    return new_str


result = upper(1)
print('result', result)


def test():
    try:
        print('123')
        1 / 0
        print('hello')
    except ZeroDivisionError as e:
        print(e)

test()


def test1():
    try:
        print('hello')
        print(name)
    except Exception as e:
        print(e)


test1()