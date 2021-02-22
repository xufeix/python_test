# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test_property.py
@time: 2021/2/22 8:18 下午
@author:XF
"""

'''
装饰器代替了get  set方法，可以直接.操作读取
'''


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误，薪水在1000--500000这个范围')


'''
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误，薪水在1000--500000这个范围')


emp1 = Employee('徐飞', 30000)
print(emp1.get_salary())
emp1.set_salary(-20000)
print(emp1.get_salary())
'''

emp1 = Employee('徐飞', 30000)
print(emp1.salary)
emp1.salary = 2000
print(emp1.salary)