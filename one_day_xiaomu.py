# /usr/bin/env python3.8
# coding:utf-8

"""
@file: one_day_xiaomu.py
@time: 2021/1/16 3:36 下午
@author:XF
"""

shop = {
    'snacks': ['薯片', '锅巴', '饼干'],
    'live': ['洗发水', '香皂', '沐浴乳'],
    'fruits': ['苹果', '香蕉', '西瓜'],
    'vegetables': ['大白菜', '西红柿', '黄瓜'],
    'drinks': ['可乐', '雪碧', '矿泉水']
}

a, b, c = 5, 10, 15
cola_pay = 2.5  # 花费时长
potato = 4
apple_two = 1.2
cabbage = 0.9  # cabbage大白菜

tot = cola_pay + potato + apple_two + cabbage + c

sport_time = 2.5
before_weight = 44.78
after_weight = 44.76

go_backhome_time = '5:00'

if __name__ == '__main__':
    print('超市柜台里有：', shop)
    print('共花费了：', tot, '元')
    print('健身之前十：', before_weight, '公斤')
    print('健身之后：', after_weight, '公斤')
    print('在', go_backhome_time, '的时候回家了')



