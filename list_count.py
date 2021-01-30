# /usr/bin/env python3.8
# coding:utf-8

"""
@file: list_count.py
@time: 2021/1/16 8:41 下午
@author:XF
"""

"""

count:返回当前列表中某个成员的个数
用法：
inttype = list.count(item)
参数：你想查询个数的元素

"""

animals = ['小猫', '小狗', '龙猫', '小猫', '鹦鹉', '小狗', '小兔子', '小猫']

cat = animals.count('小猫')
dog = animals.count('小狗')
l_cat = animals.count('龙猫')
rabbit = animals.count('小兔子')

print('我家的院子里有很多小动物，其中小猫有:%s只，小狗有:%s只，龙猫有:%s只，小兔子有:%s只' % (cat, dog, l_cat, rabbit))
print('我家的院子里有很多小动物，其中小猫有:{0}只，小狗有:{1}只，龙猫有:{2}只，小兔子有:{3}只'.format(cat, dog, l_cat, rabbit))

animals_dict = [
    {'name': 'dog'},
    {'name': 'dog'},
    {'name': 'cat'}
]

animals_dict_count = animals_dict.count({'name': 'dog'})
print('小狗在动物的字典中有{}'.format(animals_dict_count) + '只')


animals_tuple = ('小猫', '小狗', '龙猫', '小猫',
           '鹦鹉', '小狗', '小兔子', '小猫')

cat = animals_tuple.count('小猫')
dog = animals_tuple.count('小狗')
l_cat = animals_tuple.count('龙猫')
rabbit = animals_tuple.count('小兔子')

print('我家的院子里有很多小动物其中:\n小猫有:%s只\n小狗有:%s只\n龙猫有:%s只\n小兔子有:%s只' % (cat, dog, l_cat, rabbit))
