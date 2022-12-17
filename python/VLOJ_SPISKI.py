#  избавиться от вложенных циклов в коде
from itertools import product as pr
a=[1,2,3]
b=[1,2,3]
c=[1,2,3]
for i, k, j in pr(a,b,c):
    if i + k + j == 9:
        print(i, k, j)
