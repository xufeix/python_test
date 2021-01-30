# coding:utf-8

"""

数据类型之元组类型
    元组类型，如果括号里只有一个元素的时候，元素后面需要加上一个逗号，才是元组，如果不加逗号，比如tuple=（1）这个返回的类型就是int

"""

tuple_test = (1, 2, 3)
print(tuple_test)
print(type(tuple_test))

tuple01 = ()
print(type(tuple01))

print(bool((1,)))
print(len(tuple01))

max_count = max(tuple_test)
print(max_count)
min_count = min(tuple_test)
print(min_count)

