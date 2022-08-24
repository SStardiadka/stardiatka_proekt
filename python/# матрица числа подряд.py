#  матрица числа подряд
lst = list(map(int, input().split()))
matrix_zero = [[] for i in range(lst[0])]
i, l = 1, 0
while i <= lst[0] * lst[1]:
    for j in range(lst[1]):
        matrix_zero[l].append(i)
        i += 1
    l += 1
