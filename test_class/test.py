# /usr/bin/env python3.8
# coding:utf-8

"""
@file: test.py
@time: 2021/2/2 8:04 下午
@author:XF
"""


class StudentInfo(object):
    def __init__(self, studens):
        self.students = studens

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def get_all_student(self):
        for id_, value in self.students.items():
            print('学号：{},姓名：{},年龄：{},班级：{},性别：{}'.format(id_, value['name'], value['age'], value['class_number'],
                                                         value['sex']))
        return self.students

    def add(self, **kwargs):
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        id_ = max(students) + 1
        self.students[id_] = {
            'name': kwargs['name'],
            'age': kwargs['age'],
            'sex': kwargs['sex'],
            'class_number': kwargs['class_number']
        }

    def delete(self, student_id):
        if student_id not in self.students:
            print('{}不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('学号是{},{}同学已经被删除了'.format(student_id, user_info['name']))

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
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
        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return
        self.students[student_id] = kwargs
        print('同学信息更新完毕')

    def search_user(self, **kwargs):
        values = list(self.students.values())
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

    def check_user_info(self, **kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '没有发现学生年龄'
        if 'class_number' not in kwargs:
            return '没有发现学生班级'
        if 'sex' not in kwargs:
            return '没有发现学生性别'
        return True


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


if __name__ == '__main__':
    student_info = StudentInfo(students)
    user = student_info.get_by_id(1)
    student_info.add(name='dewei', age=34, sex='boy', class_number='A')
    print(student_info.students)