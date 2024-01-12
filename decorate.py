from libr.fact import factor_rec
import datetime



def time_decor(func):
    def wrapper(*arg, **kwargs):
        start = datetime.datetime.now()
        print(f'start {start}')
        res = func(*arg, **kwargs)
        end = datetime.datetime.now()
        print(f'end {end}')
        delta = end - start
        print(f'Runtime: {delta}')
        return res
    return wrapper

@time_decor
def fact_decorated(n):
    return factor_rec(n)

print(factor_rec(5))
print(fact_decorated(50))
