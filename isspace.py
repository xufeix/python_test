# /usr/bin/env python3.8
# coding:utf-8

"""
@file: isspace.py
@time: 2021/1/16 7:27 下午
@author:XF
"""
"""

isspace:判断字符串是否由一个空格组成的字符串
用法：
    booltype = string.isspace()---->无参数可传，返回一个布尔类型

istitle:判断字符是否是标题类型  此函数只用于英文
    booltype=String.istitle()---->无参数可传，返回一个布尔类型
    
isupper：判断字符串中的字母是否都是大写
islower：判断字符串中的字母是否都是小写

"""

title = 'Back Of China'
upper_str = 'PYTHON IS A GOOD CODE 哈哈！'
upper_str_02 = 'Python Is A Good Code'
lower_str = 'i love python 哈哈！'
not_empty = '    !'

print(title.istitle())
print(upper_str.istitle())
print(upper_str_02.istitle())

print('isupper', upper_str.isupper())
# print(lower_str.isupper())
print('islower', lower_str.islower())

print(not_empty.isspace())
