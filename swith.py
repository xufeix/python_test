# /usr/bin/env python3.8
# coding:utf-8

"""
@file: swith.py
@time: 2021/1/16 5:56 下午
@author:XF
"""

"""

startswith和endswith函数
startswith：判断字符串开始位是否是某成员（元素）
endswith：判断字符串结尾是否是某成员
用法：string.startswith(item)---->item想查询的某个元素，返回布尔值

"""

info = 'this is a string example!'

result = info.startswith('this')
print(result)

result = info.startswith('this is a string example!')
print(result)

print(bool(info == 'this is a string example!'))

result = info.endswith('a')
print(result)

result = info.endswith('this is a string example!')
print(result)
