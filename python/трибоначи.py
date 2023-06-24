#  трибоначи
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=" ")
    f1, f2, f3 = f2, f3, f2 + f1 + f3

n = int(input())
f1, f2, f3 = 0, 1, 1
lst = []
for i in range(n + 1):
    lst.append(f1)
    # print(f1, end=' ')
    f1, f2, f3 = f2, f3, f2 + f1 + f3
print(lst[-1])
