# /usr/bin/env python3.8
# coding:utf-8

"""
@file: replace.py
@time: 2021/1/16 6:10 下午
@author:XF
"""

"""

replace:将字符串中的old（旧元素）替换成new（新元素），并能指定替换的位置
用法：
    newstr = string.replace(old, new, max)
    参数：
        old：被替换的元素，
        new：代替old的新元素，
        max: 可选，代表替换几个，默认全部替换

"""

info = ('中文不像英文，一个单词就是一次单词，中文需要分段，一句话到底什么是主语，'
        '谓语，定语，动词，副词。需要分析和判断，我们学习中文都需要时日，计算机更需要了。'
        '而且关键词怎么分析，我们怎么知道一句话什么关键，什么不关键。所以我使用了'
        '而且关键词怎么分析，我们怎么知道一句话什么关键，什么不关键。所以我使用了'
        '而且关键词怎么分析，我们怎么知道一句话什么关键，什么不关键。所以我使用了')

a = '一个'
b = '什么'
c = '关键'
d = '*'
e = '$'
f = '@'

test = info.replace(a, d)
print(test)

# replace可以写在一行，比较方便多个敏感词需要多个字符区别去隐藏
test = info.replace(a, d).replace(b, e).replace(c, f)
print(test)