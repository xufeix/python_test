# /usr/bin/env python3.8
# coding:utf-8

"""
@file: append.py
@time: 2021/1/16 8:31 下午
@author:XF
"""

"""

用法：
list.append(new_item)
参数：
new_item:添加进列表的新的元素
被添加的元素只会加到末尾

"""

books = []
print(id(books))

books.append('python入门课程')
print(books)
print(id(books))

number = 1.1
tuple_test = (1, )
dict_test = {'name': 'xiaomu'}

books.append(number)
books.append(tuple_test)
books.append(dict_test)

books.append(1)
books.append(' ')
print(books)
print(id(books))
