#
#
# def outer(a, b):
#     print(a, b)
#     def inner(x, y):
#         print(x, y)
#         return a+b+x+y
#     return inner
#
# out = outer(1, 2)
# res = out(3, 4)

#
# def add(x, y):
#     return x+y
#
# def calculate(func, x, y):
#     return func(x, y)
#
# res = calculate(add, 1, 2)
# print(res)

#
# def decorator(func):
#     def wrapper():
#         print('dfgervc')
#         func()
#         print('2364fgreawxw')
#     return wrapper
#
# def foo():
#     print('78klo539-----')
#
# print(foo())
#
# dec = decorator(foo)
# print(dec())



#____________________________________________________________________


#
# import requests
#
# requests.status_codes()
# print(dir(requests))




# import our_func
# from our_func import f1, f2, f3
from libr.our_func import *
def output():
    f1()
    f2()
    f3()

output()

