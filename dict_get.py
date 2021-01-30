# /usr/bin/env python3.8
# coding:utf-8

"""
@file: dict_get.py
@time: 2021/1/19 5:07 下午
@author:XF
"""
"""
通过[]键取值和get取值的区别
【】取值，如果没有，就会报错，key不存在
用get取值，如果没有数据，返回结果返回none

"""

user_info = {'id': 1,
             'username': 'xiaomu',
             'password': 'abcdefg',
             'created_time': '2020-01-01 11:11:11',
             'birthday': None}

values = []
values.append(user_info['id'])
values.append(user_info['username'])
values.append(user_info['password'])
# values.append(user_info['created_time'])
values.append(user_info.get('created_time', '2020-02-02'))
# values.append(user_info['birthday'])
values.append(user_info.get('birthday', '2020-03-03'))

print(values)


