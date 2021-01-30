# /usr/bin/env python3.8
# coding:utf-8

"""
@file: zfill.py
@time: 2021/1/16 5:32 下午
@author:XF
"""

"""

zfill函数的功能是，为字符串定义长度，如不满足，缺少的部分用0填补 其中参数width需要我们传进去的宽度长度
如果定义的长度小于当前字符串的长度，则不发生变化

"""

heart = 'love'

if __name__ == '__main__':
    print(' t   ' + heart)
    print('t     ' + heart)
    print(heart.zfill(10))
    print(heart.zfill(9))
    print(heart.zfill(8))
    print(heart.zfill(6))
    print(heart.zfill(4))
