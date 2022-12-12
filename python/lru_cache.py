from functools import lru_cache
#  сокращает время выполнения конда = хеширование

@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1) + fib(n-3)

print('fib(300) =', fib(300))