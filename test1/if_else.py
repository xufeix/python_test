# /usr/bin/env python3.8
# coding:utf-8

"""
@file: if_else.py
@time: 2021/1/22 11:38 上午
@author:XF
"""

url = 'https://www.imoooc.com'

if 'www.imooc.com' in url:
    print('您进入了慕课网的世界，请好好学习')
else:
    print('请前往慕课网学习，python知识')

if 'www.imaoc.com' in url:
    _url = 'www.imooc.com'
else:
    _url = None
print('_url is %s' % _url)
