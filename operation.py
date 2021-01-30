# coding:utf-8
"""

operation 运算符
a += c # a = a+c
a -= c # a = a-c
a *= c # a = a*c
a /= c # a = a/c
a **= c # a = c的平方  幂函数
a //= c # a = a整除c

"""

a = 1
b = 2
c = 3

d = a + b + c
d += c  # d再次添加一次c
print(d)

d -= a
print(d)

d *= b  # d=d*b
print(d)

# a /= b
# print(a)

a //= b  # a = a整除b
print(a)

c %= 3  # 1可以整除返回的是0，比如c %= 2,不能被整除，返回1
print(c)

f = 10
f **= 2  # 10的平方
print(f)

list01 = [1, 2, 3]
print(list01 * 2)

tuple01 = (1, 2)
print(tuple01 * 2)

gb = 1
b = gb * 1024 * 1024 * 1024
print(b)


