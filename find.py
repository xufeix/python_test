# /usr/bin/env python3.8
# coding:utf-8

"""
@file: find.py
@time: 2021/1/16 6:05 下午
@author:XF
"""

"""

find和index函数都是你想寻找的成员的位置,从0开始算
find和index的区别：
    find：如果找不到元素，会返回-1
    index：如果找不到元素，会使程序报错

"""

info = 'python is a good code'

result = info.find('a')
print(result)

result = info.find('ok')
print(result)

result = info.index('a')
print(result)

result = info.index('ok')
print(result)  # 会报错ValueError: substring not found：值的错误：这个元素没有找到
