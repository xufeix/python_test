# /usr/bin/env python3.8
# coding:utf-8

"""
@file: format.py
@time: 2021/1/16 8:17 下午
@author:XF
"""

"""

字符串格式化

"""

print('%c' % 1020)
# print('%c' % 'aa')  # 会报错，char是指一个字符
print('%c' % 999999)

print('%u' % -1)

print('%f' % 1.2)
print('%f' % 3.14)
print('%f' % 12)

print('%d' % 10)
print('%d' % -10)
print('%d' % 1.2)

print('%s' % 123)

# print('%f' % '1.2')

print('{:d}'.format(1))
print('{:f}'.format(1.2))
