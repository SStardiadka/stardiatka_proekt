def prime_number(num):
    """
    Определяет простое ли число
    """
    if num == 2:
        return True
    s = 0
    if num > 1:
        if num % 2 != 0:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    s += 1
            if s > 0:
                return False
            return True
    return False


for i in range(100):
    if prime_number(i):
        print(i)
