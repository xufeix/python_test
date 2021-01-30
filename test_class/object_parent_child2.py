# /usr/bin/env python3.8
# coding:utf-8

"""
@file: object_parent_child2.py
@time: 2021/1/30 6:34 下午
@author:XF
"""


class XiaomuFather(object):
    def talk(self):
        print('小慕的爸爸在说话')

    def jump(self):
        print('大家都可以跳')


class XiaomuBrother(XiaomuFather):
    def run(self):
        print('小慕的哥哥在奔跑')

    def talk(self):
        print('小慕的哥哥在说话。。。。')


# 为什么我们要用多态
# 为什要用继承父类
# 答案： 为了使用已经写好的类中的函数
# 为了保留子类中某个和父类名称一样的函数的功能，这时候就用到了类的多态
# 可以帮助我们保留子类中的函数功能


class Xiaomu(XiaomuFather):
    def talk(self):
        print('hahahha,大家可以创所欲言了。。。')


if __name__ == '__main__':
    xiaomubrother = XiaomuBrother()
    xiaomubrother.run()
    xiaomubrother.talk()  # 小慕的哥哥多态了talk函数
    xiaomubrother.jump()
    xiaomufather = XiaomuFather()
    xiaomufather.talk()
    xiaomu = Xiaomu()
    xiaomu.talk()
    xiaomu.jump()
