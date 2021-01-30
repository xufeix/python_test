# /usr/bin/env python3.8
# coding:utf-8

"""
@file: iterable_test.py
@time: 2021/1/23 3:18 下午
@author:XF
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}'.format(i, j, i * j), end=' ')
    print('')


i = 0
j = 0
while i < 9:
    i += 1
    while j < 9:
        j += 1
        print('{} * {} = {}'.format(i, j, i * j), end=' ')
        if i == j:
            j = 0
            print('')
            break
