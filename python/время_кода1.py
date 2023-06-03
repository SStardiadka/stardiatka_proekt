# from timeit import timeit as tm
# def Checking_duplicates(lst: list):
#     for i in lst:
#         if lst.count(i) > 1:
#             return True
#     return False
# a = [*range(100)]
# tm('Checking_duplicates(a)')


import time

a = [*range(10000000)]
a = [1] + a
start = time.time()  ## точка отсчета времени


def check_duplicates(lst: list):
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False


print(check_duplicates(a))

end = time.time() - start  ## собственно время работы программы

print(end)  ## вывод времени
