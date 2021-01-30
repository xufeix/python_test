# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test.py
@time: 2021/1/25 8:01 下午
@author:XF
"""
"""
学生信息库
"""

students = {
    1: {'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'},
    2: {'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
        },
    3: {'name': '小云',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'},
    4: {'name': '小高',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
        },
    5: {'name': '小曼',
        'age': 18,
        'class_number': 'C',
        'sex': 'girl'}
}


def check_user_info(**kwargs):
    if 'name' not in kwargs:
        return '没有发现学生姓名'
    if 'age' not in kwargs:
        return '没有发现学生年龄'
    if 'class_number' not in kwargs:
        return '没有发现学生班级'
    if 'sex' not in kwargs:
        return '没有发现学生性别'
    return True


def get_all_studens():
    for id_, value in students.items():
        print('学号：{},姓名：{},年龄：{},班级：{},性别：{}'.format(id_, value['name'], value['age'], value['class_number'],
                                                     value['sex']))
    return students


# get_all_studens()


def add_student(**kwargs):
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    id_ = max(students) + 1
    students[id_] = {
        'name': kwargs['name'],
        'age': kwargs['age'],
        'sex': kwargs['sex'],
        'class_number': kwargs['class_number']
    }


# add_student(name='小白', age=23, sex='boy', class_number='C')
# get_all_studens()

def delete_student(student_id):
    if student_id not in students:
        print('{}不存在'.format(student_id))
    else:
        user_info = students.pop(student_id)
        print('学号是{},{}同学已经被删除了'.format(student_id, user_info['name']))


# delete_student(1)
# add_student(name='小白', age=23, sex='boy', class_number='C')
# get_all_studens()


def update_student(student_id, **kwargs):
    if student_id not in students:
        print('并不存在这个学号'.format(student_id))
    # if 'name' not in kwargs:
    #     print('没有发现学生姓名')
    #     return
    # if 'age' not in kwargs:
    #     print('没有发现学生年龄')
    #     return
    # if 'class_number' not in kwargs:
    #     print('没有发现学生班级')
    #     return
    # if 'sex' not in kwargs:
    #     print('没有发现学生性别')
    #     return
    check = check_user_info(**kwargs)
    if check != True:
        print(check)
        return
    students[student_id] = kwargs
    print('同学信息更新完毕')


update_student(1, name='dewei.zhang', age=34, class_number='D', sex='girl')
get_all_studens()


def get_user_by_id(student_id):
    return students.get(student_id)


print(get_user_by_id(3))


def search_user(**kwargs):
    values = list(students.values())
    key = None
    value = None
    result = []
    if 'name' in kwargs:
        key = 'name'
        value = kwargs[key]
    elif 'sex' in kwargs:
        key = 'sex'
        value = kwargs[key]
    elif 'class_number' in kwargs:
        key = 'class_number'
        value = kwargs[key]
    elif 'age' in kwargs:
        key = 'age'
        value = kwargs[key]
    else:
        print('没有发现搜索的关键字')
        return

    for user in values:
        if user[key] == value:
            result.append(user)
    return result


print('---------')
print(search_user(sex='girl'))




