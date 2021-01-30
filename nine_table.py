# /usr/bin/env python3.8
# coding:utf-8

"""
@file: nine_table.py
@time: 2021/1/20 7:48 下午
@author:XF
"""
"""
99乘法表
"""

work = {}

one_value = (1,)
one_key = 1
work[str(one_key)] = one_value
print(work)

two_key = 2
two_valaue = []
two_valaue.append(1)
two_valaue.append(2)
work[str(two_key)] = two_valaue

three_key = 3
three_value = []
three_value.append(1)
three_value.append(2)
three_value.append(3)
work[str(three_key)] = three_value
print(work)

four_key = 4
four_value = []
four_value.append(1)
four_value.append(2)
four_value.append(3)
four_value.append(4)
work[str(four_key)] = four_value

temp_five = (1, 2, 3, 4, 5)
five_key = 5
five_value = []
five_value.extend(temp_five)
work[str(five_key)] = five_value
print(work)

temp_six = [1, 2, 3, 4, 5, 6]
six_key = 6
six_value = []
six_value.extend(temp_six)
work[str(six_key)] = six_value

temp_seven = {1, 2, 3, 4, 5, 6, 7}
seven_key = 7
seven_value = []
seven_value.extend(temp_seven)
work[str(seven_key)] = seven_value

temp_eight = [1, 2, 3, 4, 5, 6, 7, 8]
eight_key = 8
eight_value = []
eight_value.extend(temp_eight)
eight_key = str(eight_key)
work[eight_key] = eight_value

temp_nine = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nine_key = 9
nine_value = list(temp_nine)
nine_key = str(nine_key)
work.update({nine_key: nine_value})
print(work)

_keys = work.keys()
keys = list(_keys)
print(keys)

one = keys[0]
one_value = work.pop(one)
# print(one, one_value)
print('{} * {} = {}'.format(int(one), one_value[0], int(one) * one_value[0]))

two = keys[1]
two_value = work[two]
# print(two, two_value)
print('{} * {} = {}'.format(int(two), two_value[0], int(two) * two_value[0]), end=' ')
print('{} * {} = {}'.format(int(two), two_value[1], int(two) * two_value[1]))

three = keys[2]
three_value = work[three]
# print(three, three_value)
print('{} * {} = {}'.format(int(three), three_value[0], int(three) * three_value[0]), end=' ')
print('{} * {} = {}'.format(int(three), three_value[1], int(three) * three_value[1]), end=' ')
print('{} * {} = {}'.format(int(three), three_value[2], int(three) * three_value[2]))

four = keys[3]
four_value = work.pop(four)
print('{} * {} = {}'.format(int(four), four_value[0], int(four) * four_value[0]), end=' ')
print('{} * {} = {}'.format(int(four), four_value[1], int(four) * four_value[1]), end=' ')
print('{} * {} = {}'.format(int(four), four_value[2], int(four) * four_value[2]), end=' ')
print('{} * {} = {}'.format(int(four), four_value[3], int(four) * four_value[3]))

five = keys[4]
five_value = work.pop(five)
print('{} * {} = {}'.format(int(five), five_value[0], int(five) * five_value[0]), end=' ')
print('{} * {} = {}'.format(int(five), five_value[1], int(five) * five_value[1]), end=' ')
print('{} * {} = {}'.format(int(five), five_value[2], int(five) * five_value[2]), end=' ')
print('{} * {} = {}'.format(int(five), five_value[3], int(five) * five_value[3]), end=' ')
print('{} * {} = {}'.format(int(five), five_value[4], int(five) * five_value[4]))

six = keys[5]
six_value = work.pop(six)
# print(type(six))
print('%s * %s = %s' % (six, six_value[0], int(six) * six_value[0]), end=' ')
print('%s * %s = %s' % (six, six_value[1], int(six) * six_value[1]), end=' ')
print('%s * %s = %s' % (six, six_value[2], int(six) * six_value[2]), end=' ')
print('{} * {} = {}'.format(six, six_value[3], int(six) * six_value[3]), end=' ')
print('{} * {} = {}'.format(six, six_value[4], int(six) * six_value[4]), end=' ')
print('{} * {} = {}'.format(six, six_value[5], int(six) * six_value[5]))

seven = keys[6]
seven_value = work.pop(seven)
print('{} * {} = {}'.format(seven, seven_value[0], int(seven) * seven_value[0]), end=' ')
print('{} * {} = {}'.format(seven, seven_value[1], int(seven) * seven_value[2]), end=' ')
print('{} * {} = {}'.format(seven, seven_value[2], int(seven) * seven_value[2]), end=' ')
print('{} * {} = {}'.format(seven, seven_value[3], int(seven) * seven_value[3]), end=' ')
print('{} * {} = {}'.format(seven, seven_value[4], int(seven) * seven_value[4]), end=' ')
print('{} * {} = {}'.format(seven, seven_value[5], int(seven) * seven_value[5]), end=' ')
print('{} * {} = {}'.format(seven, seven_value[6], int(seven) * seven_value[6]))

eight = keys[7]
eight_value = work.pop(eight)
print('{} * {} = {}'.format(eight, eight_value[0], int(eight) * eight_value[0]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[1], int(eight) * eight_value[1]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[2], int(eight) * eight_value[2]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[3], int(eight) * eight_value[3]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[4], int(eight) * eight_value[4]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[5], int(eight) * eight_value[5]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[6], int(eight) * eight_value[6]), end=' ')
print('{} * {} = {}'.format(eight, eight_value[7], int(eight) * eight_value[7]))

nine = keys[-1]
nine_value = work.get(nine)
format_str = '{} * {} = {}'
print(format_str.format(nine, nine_value[0], int(nine) * nine_value[0]), end=' ')
print(format_str.format(nine, nine_value[1], int(nine) * nine_value[1]), end=' ')
print(format_str.format(nine, nine_value[2], int(nine) * nine_value[2]), end=' ')
print(format_str.format(nine, nine_value[3], int(nine) * nine_value[3]), end=' ')
print('{} * {} = {}'.format(nine, nine_value[4], int(nine) * nine_value[4]), end=' ')
print('{} * {} = {}'.format(nine, nine_value[5], int(nine) * nine_value[5]), end=' ')
print('{} * {} = {}'.format(nine, nine_value[6], int(nine) * nine_value[6]), end=' ')
print('{} * {} = {}'.format(nine, nine_value[7], int(nine) * nine_value[7]), end=' ')
print('{} * {} = {}'.format(nine, nine_value[-1], int(nine) * nine_value[-1]))
