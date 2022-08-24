def matr_ix(n):
    matrix = [list(map(int, input().split()))
    for i in range(n)]  # создаем квадратную матрицу
    return matrix


n = int(input())
lst = []
matr = matr_ix(n)
for i in range(len(matr)):
    for j in range(len(matr)):
        if i > j and i < n - 1 - j or i < j and i > n - 1 - j:  # находим элементы на западе и востоке
            lst.append(matr[i][j])  # добавляем в список
for i in range(len(matr)):
    for j in range(len(matr)):
        if i == j or i + j + 1 == n or j == n - i - 1:  # находим элементы на главной и побочной диоганалях
            lst.append(matr[i][j])  # добавляем в список
print(max(lst))  # выводим максимум
#  if i >= j and i <= n-1-j or i <= j and i >= n-1-j: можно обьеденить....
