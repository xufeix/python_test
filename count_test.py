# /usr/bin/env python3.8
# coding:utf-8

"""
@file: count_test.py
@time: 2021/1/16 5:41 下午
@author:XF
"""

"""

count的功能：返回当前字符串中某个成员（元素）的个数
如果查询成员（元素）不存在，则返回0

"""

info = '''
    Beauty
    
    There were a sensitivity and a beauty to her that have nothing to do with looks. 
    She was one to be listened to, whose words were so easy to take to heart.
    
    It is said that the true nature of being is veiled. 
    The labor of words, the expression of art, the seemingly ceaseless buzz that is human thought all have in common the need to get at what really is so. 
    The hope to draw close to and possess the truth of being can be a feverish one. 
    In some cases it can even be fatal, if pleasure is one's truth and its attainment more important than life itself. 
    In other lives, though, the search for what is truthful gives life.

'''

a = info.count('a')
b = info.count('b')
c = info.count('c')
d = info.count('d')

print(a, b, c, d)

number_list = [a, b, c, d]
print(number_list)

print('在列表中最大的数值是：', max(number_list))

number_dict = {
    'a': a,
    'b': b,
    'c': c,
    'd': d
}

print('每个成员对应的数值分别是：', number_dict)
