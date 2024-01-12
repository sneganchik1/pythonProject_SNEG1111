# var = 10
# print(var)
#
# def func(var):
#     var += 1
#     print(f' var in func {var}')
#     return var
#
# var = func(var)
# print(var)
#

# n! = n*f(n-1)

#----------------------------------------------------

# def factor_rec(n):
#     if n in (0,1):
#         return 1
#     return n * factor_rec(n-1)
#
# print(factor_rec(4))

#----------------------------------------------------

#
# lst = [1, 2, 3, [4, 5, 6]]
#
# def rec(lst):
#     for i in lst:
#         print (i)
#         print(type(i))
#         if type(i) is list:
#             return rec(i)
#
# rec(lst)
# a = 'abc'
# print(type(a))
# print(a is str)

# ----------------------------------------
# числами Фибоначчи. Это ряд чисел, каждое из которых равняется сумме двух предыдущих: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 и так далее.
# F(N) = F(N - 1)+F(N-2)

#
# def fibo_rec(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#
#         # f(n) = f(n - 1) + f(n - 2)
#         return fibo_rec(n-1) + fibo_rec(n-2)
#
# print(fibo_rec(8))
#
#
# def fibo(n):
#     fib1=fib2=1
#     if n in (1, 2):
#         return fib1
#     for i in range(n-2):
#         fib1, fib2=fib2, fib1+ fib2
#     return fib2
#
# print(fibo(9))


# print(dir())


l = [1, 2, 3, 6, 7, 8, 5, 9]

def sum_l(l):
    if l == []:
        return 0
    else:
        sum = sum_l(l[1:])
        sum = sum +l[0]
        return sum
l1 = [1, 2, 3]
print(sum_l(l1))