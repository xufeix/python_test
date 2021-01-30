# /usr/bin/env python3.8
# coding:utf-8

"""
@file: list_index.py
@time: 2021/1/17 4:16 下午
@author:XF
"""

"""

index:本节课时列表的索引获取与修改
[3:8]:左含右不含

"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(numbers) - 1)
print(numbers[9])
print(id(numbers))

print('获取列表完整数据', id(numbers[:]))
print('另一种获取列表完整数据的方法', numbers[0:])
print('第三种获取列表数据的方法', numbers[:-1])

print('列表的反序', numbers[::-1])
print('列表的反向获取', numbers[-3:-1])

print('通过步长获取切片：', numbers[0: 8: 2])

print('通过切片生成空列表', numbers[0: 0])

new_numbers = numbers[: 4]
print(new_numbers)


numbers[3] = 'code'
print(numbers)

# numbers[10] = 1
# print(numbers)

numbers[2: 5] = ['a', 'b', 'c']
print(numbers)

print(numbers.index('c'))

item = numbers.pop(4)
print(item, numbers, len(numbers))

del numbers[4]
print(numbers)

tuple_test = (1, 2, 3)
# del tuple_test[2]
# del tuple_test
# print(tuple_test)
