# import libr.our_func
#
#
# def print_fun():
#     libr.our.func.f1()
#     libr.our.func.f2()
#     libr.our.func.f3()
#
#
# print(print_fun())   NEPRAVILNO!!!!
# __________________________________________________
# def print_func(a, b):
#     """
#     function for adding a + b
#     :param a: str/int
#     :param b: str/int
#     :return: str/int
#     """
#
#     res = {a + b}
#     print(f'res = {res}')
#     return res
# print(print_func.__doc__)
#_______________________________________________________

# var: int = '3'
# def print_func(a: int, b: int) -> int:
#     """
#     function for adding a + b
#     :param a: str/int
#     :param b: str/int
#     :return: str/int
#     """
#
#     res = {a + b}
#     print(f'res = {res}')
#     return res
#
# print(print_func(2, 4))
# print(print_func.__doc__)

#_______________________________________________________

# a = int('123')
#
# print(a, type(a))
#
# def func(v):
#     return v % 2
#
# res = min([1, 2 , 5 , 8, -2], key=func)
# print(f'res = {res}')
#
# res1 = max([1, 2 , 5 , 8, -2], key=func)
# print(f'Max = {res1}')
#
#
# print(f'Min: {res}, Max: {res1}')



#_______________________________________________________

#
# def foo(x):
#     return x % 2
#
# res = min([1, 2 , 5 , 8, -2], key=lambda x: x % 2)
# print(f'res = {res}')
#
# print(foo(5))
#
#
# # print(lambda x: x % 2)

#_______________________________________________________
#
# lst = [1, 2, 3, 4, 5, 6]
# def func(lst):
#     if lst % 2 == 0:
#         return True
#     # else:
#     return False #tak tozhe mozhno
#
# sep_slt = filter(func, lst)
#
# print(lst)
# print(list(sep_slt))   #если без оборота в лист, то print (sep_slt) выдаст объект, а не цифры
#
# #_______________________________________________________
#
# lst = [1, 2, 3, 4, 5, 6]
#
# def func(lst):
#     res = lst + 1
#     return res
#
# map_f = map(func, lst)
# print(list(map_f)) #если без оборота в лист, то print (map_f) выдаст объект, а не цифры
#
# # #_______________________________________________________
#
# lst = [1, 2, 3, 4, 5, 7]
# lst1 = ['a', 'b', 'c', 'd']
# lst2 = [6, 7, 8, 9]
# #(1, 'a'), (2:'b')
#
# ziped = zip(lst, lst1, lst2)
# print(list(ziped))
# for i in ziped:
#     print(i)


# # #_______________________________________________________

a = int(input('number 0-9  '))
b = int(input('number 0-9  '))
c = input(' * or + ')
def calc(a, b, c):
    """

    :param a: int
    :param b: int
    :param c: str
    :return: int
    """
    if c == '*' :
        res = a * b
        # return res
    elif c == '+' :
        res = a + b

    else:
        print('check conditionals')
        res = []
    return res


print(calc(a, b, c))
