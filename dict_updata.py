# /usr/bin/env python3.8
# coding:utf-8

"""
@file: dict_updata.py
@time: 2021/1/17 6:27 下午
@author:XF
"""

"""

update和setdefault

"""

user = {'username': 'xiaomu', 'age': 19}
xiaomu = {'username': '小慕', 'age': 10, 'top': 176, 'sex': '女'}

user.update(xiaomu)
print(user)

value = user.setdefault('username', 'xiayun')
value = user.setdefault('birthday', '2020-1-1')
print(user, value)

# user['top'] = 174
# print(user)
#
# user['username'] = '小慕'
# user['age'] = 10
# print(user)
