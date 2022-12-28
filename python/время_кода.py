import timeit
lst1 = '''map(lambda x: int(x), range(1000))'''
lst2 = '''({i:i+1 for i in range(100)})'''
x = timeit.timeit(lst1)
y = timeit.timeit(lst2)
print(f'{x}\n{y}')