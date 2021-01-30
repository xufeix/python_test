# /usr/bin/env python3.8
# coding:utf-8

"""
@file: set_init.py
@time: 2021/1/19 8:46 下午
@author:XF
"""
"""
集合:去重，保留唯一性
"""

a = set()
print(a)
print(type(a))

b = set(['python', 'django', 'flask'])
print(b)

c = {(1, 2, 3), '123', 1}
print(c)
'python', 'django', 'flask'
d = {}
print(d, type(d))

a_list = ['python', 'django', 'flask', 'python']
b_set = set(a_list)
print(b_set)
