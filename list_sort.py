# /usr/bin/env python3.8
# coding:utf-8

"""
@file: list_sort.py
@time: 2021/1/17 3:55 下午
@author:XF
"""

"""

sort:排序，不写参数默认正序

"""

shu = '01老鼠'
niu = '02牛'
hu = '03老虎'
tu = '04兔'
long = '05龙'
she = '06蛇'
ma = '07马'
yang = '08羊'
hou = '09猴'
ji = '10鸡'
gou = '11狗'
zhu = '12猪'

shengxiao = []

shengxiao.append(gou)
shengxiao.append(zhu)
shengxiao.append(ji)
shengxiao.append(she)
shengxiao.append(tu)
shengxiao.append(hou)
shengxiao.append(hu)
shengxiao.append(niu)
shengxiao.append(shu)
shengxiao.append(long)
shengxiao.append(ma)
shengxiao.append(yang)

print(shengxiao)
print(len(shengxiao))

shengxiao.sort()
print(shengxiao)

shengxiao.sort(reverse=True)
print(shengxiao)

shengxiao.sort(reverse=True)
print(shengxiao)

# mix = ['python', 1, 2, {'name': '小慕'}]
# mix.sort()
# print(mix)


