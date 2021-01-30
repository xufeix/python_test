# /usr/bin/env python3.8
# coding:utf-8

"""
@file: capitalize.py
@time: 2021/1/16 4:56 下午
@author:XF
"""

"""

capitalize:首字母大写
string字符串类型里的capitalize函数
变量.函数()通用叫法叫做函数的调用
eg:如果首字母已经是大写的了，用户这个函数也是无效的
首字母是数字或者中文，用这个函数无效

"""

name = 'xiao mu'
info = 'hello 小慕'
_info = '小慕 hello'
number_str = '1234'

new_name = name.capitalize()
new_info = info.capitalize()
_new_info = _info.capitalize()
new_number_str = number_str.capitalize()

print(new_name, name)
print(new_info, info)
print(_new_info, _info)
print(new_number_str, number_str)
