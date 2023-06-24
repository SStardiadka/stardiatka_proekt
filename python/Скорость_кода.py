class Speed:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self):
        import time

        start = time.time()  ## точка отсчета времени
        self.fun()
        end = time.time()  ## собственно время работы программы

        print(f"Скорость выполнения кода ({end - start})")  ## вывод времени


matr = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]


@Speed
def count_zeros() -> list:
    lst = [*range(10_000_000)]
    lst = [str(i) for i in lst]
    return lst


@Speed
def count_zeros1() -> int:
    s = 0
    for i in matr:
        for j in i:
            if j == 1:
                s += matr.index(i)
                break
    return s


count_zeros1()
count_zeros()
