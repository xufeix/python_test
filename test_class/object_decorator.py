# /usr/bin/env python3.8
# coding:utf-8

"""
@file: object_decorator.py
@time: 2021/1/28 5:18 下午
@author:XF
"""


def check_str(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is {}'.format(result)
        else:
            return 'result is failed'.format(result)

    return inner


@check_str
def test(data):
    return data


result = test('no')
print(result)

result = test('ok')
print(result)
