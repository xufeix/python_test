# /usr/bin/env python3.8
# coding:utf-8

"""
@file: iterable_for2.py
@time: 2021/1/23 2:52 下午
@author:XF
"""

a = [1, 2, 3]
b = [4, 5, 6]

for i in a:
    print(i)
    print('.............')
    for j in b:
        print(i + j)
    print('--------')

print(i , j)