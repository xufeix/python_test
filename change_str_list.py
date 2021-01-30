# /usr/bin/env python3.8
# coding:utf-8

"""
@file: change_str_list.py
@time: 2021/1/20 3:15 下午
@author:XF
"""

"""
字符串与list之间的转换
注意，split不可以传空字符串
使用join，需要注意数据不可以是数字,字典，元组
"""

a = 'abc'

print(a.split())

b = 'a,b,cd'
print(b.split(','))

c = 'a|b|c|d'
print(c.split('|', 1))

d = 'a~b~c'
# print(d.split(''))  # 不可以传空字符串


test = ['a', 'b', 'c']
test_str = '|'.join(test)
print(test_str)

# test2 = [1.1, 2, 3]
# print('|'.join(test2))

# test3 = [{'name': 'dewei'}, {'name': 'xiaomu'}]
# print('.'.join(test3))

sort_str = 'a b d f i p q c'
sort_list = sort_str.split(' ')
print(sort_list)

sort_list.sort()  # sort()字符串按26个字母顺序排序方法
print(sort_list)
sort_str = ' '.join(sort_list)
print(sort_str)

sort_str_new = 'abdfipqc'
res = sorted(sort_str_new)  # 字符串转换成列表
print(res)
print(''.join(res))  # 列表转换成字符串
