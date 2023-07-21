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


def prime_number(num):
    """
    Определяет простое ли число
    """
    if num == 2:
        return True
    s = 0
    if num > 1:
        if num % 2 != 0:
            for i in range(3, int(num ** (1 / 2)), 2):
                if num % i == 0:
                    s += 1
            if s > 0:
                return False
            return True
    return False


@Speed
def get():
    for i in range(1_00000):
        if prime_number(i):
            print(i)


get()
