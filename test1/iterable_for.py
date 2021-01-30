# /usr/bin/env python3.8
# coding:utf-8

"""
@file: iterable_for.py
@time: 2021/1/22 3:13 下午
@author:XF
"""

users = {'name': 'dewei', 'age': 30}

for i in users:
    print(i, users[i])

item = users.items()
print(item)

for key, value in users.items():
    print(key, value)

users_list = [
    {'name': 'dewei'},
    {'name': 'xiaomu'}
]

for user in users_list:
    print(user.get('name'))
    print(user.get('age'))

l = range(6)
print(l)

for i in l:
    print(i)
else:
    print('for循环结束了')

