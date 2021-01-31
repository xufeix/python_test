# /usr/bin/env python3.8
# coding:utf-8

"""
@file: object_parent_chlid3.py
@time: 2021/1/31 10:18 下午
@author:XF
"""


class Tool(object):
    def wolk(self):
        return 'tool work'

    def car(self):
        return 'car will run'


class Food(object):
    def wolk(self):
        return 'food wolk'

    def cake(self):
        return 'i like cake'


# 集成父类的子类
class Person(Food, Tool):
    pass


if __name__ == '__main__':
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    print(p_car)
    print(p_cake)
    p_wolk = p.wolk()
    print(p_wolk)
    print(Person.__mro__)  # 查看集成列
