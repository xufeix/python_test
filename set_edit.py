# /usr/bin/env python3.8
# coding:utf-8

"""
@file: set_edit.py
@time: 2021/1/20 11:41 上午
@author:XF
"""
"""
set集合无序的，无法通过索引来获取元素，可以通过for循环来获取
用update内置函数时需要注意，可以使用update添加一些元组列表，字典等。但不能是字符串，否则会拆分
"""

a_list = ['python', 'django', 'django', 'flask']

a_set = set()

a_set.add(a_list[0])
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[-1])

print(a_set)

a_set.add(True)
a_set.add(None)
print(a_set)

a_tuple = ('a', 'b', 'c')
a_set.update(a_tuple)
print(a_set)

a_set.update('python')
print(a_set)

a_set.remove('python')
print(a_set)

a_set.clear()
print(a_set)

# del a_set
print(a_set)

lst = [1, 2, 3, 1]
res = {"a", "b", "c", "d"}
res.update(lst)

print(res)
