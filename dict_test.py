# coding:utf-8

"""

数据类型之字典

"""

user_info = {'name': '小慕同学', 'age': 10, 'top': '180cm'}

result = 'name' in user_info  # in 成员运算符
print(result)

result = 'hope' in user_info
print(result)

result = 'hope' not in user_info
print(result)

count = len(user_info)
print(count)

result_bool = bool(user_info)
print(result)

empty_dict = {}
print(bool(empty_dict))

print(type(empty_dict))

print(max(user_info))
print(min(user_info))
