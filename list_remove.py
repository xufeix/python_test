# /usr/bin/env python3.8
# coding:utf-8

"""
@file: list_remove.py
@time: 2021/1/16 8:59 下午
@author:XF
"""

"""

remove:删除列表中的某个元素
用法：
list.remove(item)
参数：
item:准备删除的列表元素

del:把变量完全删除

"""

shops = ['可乐', '洗发水', '可乐', '牛奶', '牛奶', '牙膏', '牙膏']

print('我们超市有这些内容:%s' % shops)
print('我们的可乐有：%s件产品' % shops.count('可乐'))
print('我们的牛奶有：%s件产品' % shops.count('牛奶'))
print('我们的牙膏有：%s件产品' % shops.count('牙膏'))
print('我们的洗发水有：%s件产品' % shops.count('洗发水'))

print('我们要购买意见洗发水')
shops.remove('洗发水')
print('现在我们的洗发水还剩下%s件，当前已经没有洗发水了' % shops.count('洗发水'))

# shops.remove('洗发水')  # 报错，删除list里没有的数据，会报错 x not is list


del shops

print(shops)  # 报错，shops没有被定义  name 'shops' is not defined

