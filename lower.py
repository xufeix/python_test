# /usr/bin/env python3.8
# coding:utf-8

"""
@file: lower.py
@time: 2021/1/16 5:11 下午
@author:XF
"""

"""

lowerhe 和 casefold函数都是是字符串变为小写函数
casefold支持更多国家的预言

"""

message_en = 'How do you do ? Xiao mu'
message_ch = '你好呀，iaomu'
message_mix = '你好呀，XiaoMu，今天是星期三！'

message_en_lower = message_en.lower()
message_en_casefold = message_en.casefold()

message_ch_lower = message_ch.lower()
message_ch_casefold = message_ch.casefold()

message_mix_lower = message_mix.lower()
message_mix_casefold = message_mix.casefold()

print(message_en_lower, message_en_casefold)
print(message_ch_lower, message_ch_casefold)
print(message_mix_lower, message_mix_casefold)

empty = ''  # 空字符串使用小写字母的函数不会报错
empty_lower = empty.lower()
empty_casefold = empty.casefold()

print('.' + empty_lower + '.', '.' + empty_casefold + '.')

'''

注意：字符串是不可变的，使用了小写函数后，是新的值，不会影响原始的值

'''
