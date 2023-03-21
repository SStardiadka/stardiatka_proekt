from timeit import timeit
from sys import setrecursionlimit, set_int_max_str_digits


def stepen(a, b, d=1):
    for i in range(b):
        b -= 1
        d *= a
        return stepen(a, b, d)
    return d


set_int_max_str_digits(2000000)
setrecursionlimit(2000000)
print(stepen(1123456123456, 10000))
print(
    f"Среднее время вычисления: "
    f"{round(timeit('stepen(1123456123456, 10000)', number=10, globals=globals()) / 10, 6)} с."
)
