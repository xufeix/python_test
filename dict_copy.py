# /usr/bin/env python3.8
# coding:utf-8

"""
@file: dict_copy.py
@time: 2021/1/19 7:51 下午
@author:XF
"""

fruits = {'apple': 30,
          'banana': 50,
          'pear': 100
          }

real_fruits = fruits.copy()
print(real_fruits)

real_fruits['orange'] = 50
real_fruits.update({'cherry': 100})

print(real_fruits)
print(fruits)

real_fruits['apple'] = real_fruits['apple'] - 5
print(real_fruits)

real_fruits['pear'] -= 3
print(real_fruits)

real_fruits.clear()
print(real_fruits)

print('第二天')
real_fruits = fruits.copy()
print(real_fruits)