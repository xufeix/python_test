# /usr/bin/env python3.8
# coding:utf-8

"""
@file: def_while.py
@time: 2021/1/25 4:34 下午
@author:XF
"""
count = 0


def test():
    global count  # 生命全局变量
    count += 1
    if count != 5:
        print('count条件不满足，我要重新执行我自己！当前 count是{}'.format(count))
        return test()
    else:
        print('count的值是{}'.format(count))


test()
