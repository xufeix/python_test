# /usr/bin/env python3.8
# coding:utf-8

"""
@file: dict_popitem.py
@time: 2021/1/19 8:11 下午
@author:XF
"""

students = {'dewei': '到', 'xiaomu': '在', 'xiaoyun': '在呢', 'xiaogao': '在'}

print('xiaogao在吗？')
xiaogao = students.popitem()
print('{}喊{}'.format(xiaogao[0], xiaogao[1]))
xiaoyun = students.popitem()
print('{}喊{}'.format(xiaoyun[0], xiaoyun[1]))
print(xiaoyun)
xiaomu = students.popitem()
print('{}喊{}'.format(xiaomu[0], xiaomu[1]))
dewei = students.popitem()
print('{}喊{}'.format(dewei[0], dewei[1]))

print(students)

# students.popitem()