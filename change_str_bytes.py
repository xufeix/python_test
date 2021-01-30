# /usr/bin/env python3.8
# coding:utf-8

"""
@file: change_str_bytes.py
@time: 2021/1/20 5:26 下午
@author:XF
"""

a = 'heelo xiaomu'

print(a, type(a))

b = b'hello xiaomu'
print(b, type(b))

print(b.capitalize())

print(b.replace(b'xiaomu', b'dewei'))
print(b[0])
print(b[3])
print(b[:3])
print(b.find(b'x'))

print(dir(b))

# c = b'hello 小慕'
# print(c)

c = 'hello 小慕'
d = c.encode('utf-8')
print(d, type(d))
print(d.decode('utf-8'))

