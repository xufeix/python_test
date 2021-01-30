# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test.py
@time: 2021/1/25 10:43 上午
@author:XF
"""
"""
根据业务需求，现要求慕友们开发一个货币兑换的服务系统，具体要求如下：
 1、实现人民币兑换美元的功能
 2、实现美元兑换人民币的功能
 3、实现人民币兑换欧元的功能
 4、1美元=7.06人民币，1人民币=0.12欧元
 5、在兑换后保留2位小数
 6、在输入要选择服务后有波浪线分隔；本次兑换服务结束后有等号线进行分隔。
"""
rmb_m = '1、人民币兑换美元的功能'
m_rmb = '2、美元兑换人民币的功能'
rmb_o = '3、人民币兑换欧元的功能'
print(rmb_m)
print(m_rmb)
print(rmb_o)

a = 0
b = 0

for i in range(4):
    d = int(input('请输入想选择的项目：'))

    if d == 1:
        how = int(input('请输入你想兑换的数量：'))
        b = how / 7.061
        print('可兑换美元为：{:.2f}'.format(b))
    elif d == 2:
        how = int(input('请输入你想兑换的数量：'))
        b = how * 7.06
        print('可兑换人民币为：{}'.format(b))
    elif d == 3:
        how = int(input('请输入你想兑换的数量：'))
        b = how * 0.12
        print('可兑换欧元为：{:.2f}'.format(b))
    else:
        print('请重新选择服务项目')

