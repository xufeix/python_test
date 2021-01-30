# /usr/bin/env python3.8
# coding:utf-8

"""
@file: iterable_handle.py
@time: 2021/1/23 3:09 下午
@author:XF
"""

users = [
    {'username': 'dewei', 'age': 33, 'top': 175, 'sex': '男'},
    {'username': '小慕', 'age': 1, 'top': 175, 'sex': '男'},
    {'username': 'xiaoyun', 'age': 18, 'top': 175, 'sex': '女'},
    {'username': 'dewei', 'age': 33, 'top': 188, 'sex': '男'}
]

man = []
for user in users:
    if user.get('sex') == '女':
        continue
    man.append(user)
    print('%s加入了帮忙的行列' % user.get('username'))

print(man)

l = range(100)
for i in l:
    if i == 80:
        print('-------')
        print('已经循环了80次了')
        # break
    print(i)
else:
    print('循环正常退出了')
