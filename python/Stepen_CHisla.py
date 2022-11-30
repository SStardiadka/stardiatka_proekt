def stepen(a,b, d =1):
    for i in range(b):
        b -=1
        d*=a
        return stepen(a, b,d)
    return d
print(stepen(2, 10))
#  степень числа рекурсия