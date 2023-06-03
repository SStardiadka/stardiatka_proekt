def stepen(a, b, d=1):
    for _ in range(b):
        b -= 1
        d *= a
        return stepen(a, b, d)
    return d


lst = []
for i in range(1, 21):
    lst.append(stepen(2, i))
print(lst)
#  степень числа рекурсия
