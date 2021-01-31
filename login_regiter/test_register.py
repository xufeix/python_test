# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_register.py
@time: 2021/1/30 9:14 下午
@author:XF
"""

"""
数据库连接与操作
"""

import pymysql

# 注册
name = input("请输入姓名：")
passwd = input("请输入秘密：")

# 插入数据库

register_sql = "insert into user_account(`name`,`passwd`) values('" + name + "','" + passwd + "')"

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', user= 'root', password='', database='user_account')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
print(cursor.execute(register_sql))

db.commit()

