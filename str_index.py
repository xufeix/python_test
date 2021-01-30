# /usr/bin/env python3.8
# coding:utf-8

"""
@file: str_index.py
@time: 2021/1/17 4:45 下午
@author:XF
"""
"""

字符串的索引

"""

name = "xiaomu"

temp = []
# temp.append(name[0])
# temp.append(name[1])
# temp.append(name[2])
# temp.append(name[3])
# temp.append(name[4])
# temp.append(name[5])

temp.extend(name)
print(temp)

temp.reverse()  # 反序展示
print(temp)


new_name = name[:: -1]
print(new_name)

result = new_name.find('mu')
# result = new_name.index('mu')
print(result)

