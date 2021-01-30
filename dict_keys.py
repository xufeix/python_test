# /usr/bin/env python3.8
# coding:utf-8

"""
@file: dict_keys.py
@time: 2021/1/18 2:19 下午
@author:XF
"""

"""获取字典里所有key"""

project = {'id': 1, 'project_name': 'ipad', 'price': 2200, 'cunt': 30}

project_title = list(project.keys())

print(project_title[0])
print(project_title[3])
print(project_title[2: 6])

project_title.append('user')
print(project_title)

# print(project[0])