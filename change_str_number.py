# /usr/bin/env python3.8
# coding:utf-8

"""
@file: change_str_number.py
@time: 2021/1/20 2:49 下午
@author:XF
"""

int_data = 12
float_data = 3.14

str_int_data = str(int_data)
str_float_data = str(float_data)

print(str_int_data, type(str_int_data), str_float_data, type(str_float_data))

str_float = '3.14'
str_int = '123456'

real_float = float(str_float)
real_int = int(str_int)

print(real_float, type(real_float), real_int, type(real_int))

float_data_str = '3.14'
test_data = float(float_data_str)
print(test_data)

int_data_str = '123'
test_data = float(int_data_str)
print(test_data, type(test_data))

