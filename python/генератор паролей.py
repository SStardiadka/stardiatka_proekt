#   генератор паролей
from random import shuffle, choice
lst_matr = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', ],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], ['2', '3', '4', '5', '6', '7', '8', '9']]
lst =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '8', '9']
m, lm = int(input()), int(input())
lst_par = [[] for _ in range(m)]
for i in range(m):
    for j in range(3):
        lst_par[i].append(choice(lst_matr[j]))
for i in range(m):
    for j in range(lm - 3):
        lst_par[i].append(choice(lst))
for i in lst_par:
    shuffle(i)
    print(*i, sep='')
