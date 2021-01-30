# /usr/bin/env python3.8
# coding:utf-8

"""
@file: set_inter.py
@time: 2021/1/20 2:21 下午
@author:XF
"""
"""
set的交集

"""

a = ['dewei', 'xiaomu', 'xiaohua', 'xiaoguo']
b = ['xiaohua', 'dewei', 'xiaoman', 'xiaolin']
c = ['xiaoguang', 'xiaobai', 'dewei', 'xiaoyuan']

a_set = set(a)
b_set = set(b)
c_set = set(c)

print(a, b, c)

result = a_set.intersection(b_set, c_set)
print(result)
xiaotou = list(result)

print('{}谁是这个小偷'.format(xiaotou[0]))