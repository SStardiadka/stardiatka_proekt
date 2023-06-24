def matr_ix():  # юго- запад матрицы
    matrix = [list(map(int, input().split())) for i in range(int(input()))]
    return matrix


lst = []
lslst = matr_ix()
for i in range(len(lslst)):
    lst.append(max(lslst[i][0:i+1]))
print(max(lst))
