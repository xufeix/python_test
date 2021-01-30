# /usr/bin/env python3.8
# coding:utf-8

"""
@file: set_diff.py
@time: 2021/1/20 2:13 下午
@author:XF
"""
"""
set内置函数差集
"""

drivers = ['sewei', 'xiaomu', 'xiaoming', 'xiaoman']
testers = ['xiaomu', 'xiaoman', 'xiaogang', 'xiaotao']

diver_set = set(drivers)
test_set = set(testers)

sample_drivers = diver_set.difference(test_set)
print(sample_drivers)