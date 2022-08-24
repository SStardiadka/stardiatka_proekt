# бросить монетку
from random import *
lst1 = []
lst = [0, 1, 0, 1, 0, 1, 0, 1]
orresh = {0: "'ОРЕЛ'", 1: "'РЕШКА'"}
shuffle(lst)
for i in range(1000):
    lst1.append(orresh[choice(lst)])
print(f'*****  {max(lst1, key=lambda x: lst1.count(x))}  *****')
shuffle(lst)
