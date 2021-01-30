# /usr/bin/env python3.8
# coding:utf-8

"""
@file: set_isdisjoint.py
@time: 2021/1/20 2:33 下午
@author:XF
"""

"""
isdisjoint判断两个集合包含相同的元素，如果没有返回True否则返回false
用法：
a_set.isdisjoint(b_set)

"""

company_not_allow = {'女', '喝酒', '抽烟', '睡懒觉'}

one_player = {'男', '跑步', '朝气', '喝酒'}
two_player = {'女', '生活规律', '跆拳道'}
three_player = {'男', '太极拳'}
four_palyer = {'男', '空手道', '年轻'}

print(company_not_allow.isdisjoint(one_player))
print(company_not_allow.isdisjoint(two_player))
print(company_not_allow.isdisjoint(three_player))
print(company_not_allow.isdisjoint(four_palyer))
