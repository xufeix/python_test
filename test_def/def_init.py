# /usr/bin/env python3.8
# coding:utf-8

"""
@file: def_init.py
@time: 2021/1/25 3:48 下午
@author:XF
"""


def capitalize(data):
    index = 0
    temp = ''
    for item in data:
        if index == 0:
            temp = item.upper()
        else:
            temp += item
        index += 1
    print('for结束了')
    return temp
    print('finish')


result = capitalize('hello,小慕')
print(result)


def massage(message, message_type):
    new_message = '[%s] %s' % (message_type, message)
    print(new_message)


result = massage(message='今天天气真不好', message_type='info')


def test():
    for i in range(10):
        if i == 5:
            return i


print(test())



