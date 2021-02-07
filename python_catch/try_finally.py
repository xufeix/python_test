# /usr/bin/env python3.8
# coding:utf-8

"""
@file: try_finally.py
@time: 2021/2/7 5:37 下午
@author:XF
"""


def test1():
    try:
        1 / 0
    except Exception as e:
        print(e)
    finally:
        return 'finally'


result = test1()
print(result)

print('__-----------------')


def test2():
    try:
        1 / 0
    except Exception as e:
        print('111111')
        return e
    finally:
        print('finally')


result = test2()
print(result)


def test3():
    try:
        print('test 111')
        return 'try'
    except Exception as e:
        print('e')
    finally:
        print('finally test')


print('------------')
result = test3()
print(result)