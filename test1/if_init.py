# /usr/bin/env python3.8
# coding:utf-8

"""
@file: if_init.py
@time: 2021/1/21 5:27 下午
@author:XF
"""
info = 'my name is xiaomu'

info_list = info.split()
print(info_list)

if info_list[0] == 'xiaomu':
    info_list[0] = 'dewei'

if info_list[1] == 'xiaomu':
    info_list[1] = 'dewei'

if info_list[2] == 'xiaomu':
    info_list[2] = 'dewei'

if info_list[-1] == 'xiaomu':
    info_list[-1] = 'dewei'

print(info_list)

info = ' '.join(info_list)
print(info)

info = 'my name is dewei, i am a pythoner, i love python'
info_list = info.split()

if info_list[0] in ['python', 'i']:
    info_list[0] = '*'

if info_list[1] == 'python' or info_list[1] == 'i':
    info_list[1] = '*'

if info_list[2] == 'python' or info_list[2] == 'i':
    info_list[2] = '*'

if info_list[3] == 'python' or info_list[3] == 'i':
    info_list[3] = '*'

if info_list[4] == 'python' or info_list[4] == 'i':
    info_list[4] = '*'

if info_list[5] == 'python' or info_list[5] == 'i':
    info_list[5] = '*'

if info_list[6] == 'python' or info_list[6] == 'i':
    info_list[6] = '*'

if info_list[7] == 'python' or info_list[7] == 'i':
    info_list[7] = '*'

if info_list[8] == 'python' or info_list[8] == 'i':
    info_list[8] = '*'

if info_list[9] == 'python' or info_list[9] == 'i':
    info_list[9] = '*'

if info_list[-1] in ['python', 'i']:
    info_list[-1] = '*'

print(info_list)

info = ' '.join(info_list)
print(info)

info = 'my name is dewei'
print(len(info))

if len(info) > 10 and len(info) != 16:
    print(info.replace('dewei', 'xiaomu'))

print('finish ')